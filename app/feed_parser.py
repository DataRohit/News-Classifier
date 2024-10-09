from datetime import datetime

import feedparser

from app.celery_tasks import process_article
from app.database import add_article_to_db

RSS_FEEDS = [
    "http://rss.cnn.com/rss/cnn_topstories.rss",
    "http://qz.com/feed",
    "http://feeds.foxnews.com/foxnews/politics",
    "http://feeds.reuters.com/reuters/businessNews",
    "http://feeds.feedburner.com/NewshourWorld",
    "https://feeds.bbci.co.uk/news/world/asia/india/rss.xml",
]


def parse_feeds():
    seen_urls = set()
    for feed_url in RSS_FEEDS:
        feed = feedparser.parse(feed_url)
        for entry in feed.entries:
            if entry.link not in seen_urls:
                seen_urls.add(entry.link)
                article = {
                    "title": entry.title,
                    "content": (
                        entry.content[0].value if "content" in entry else entry.summary
                    ),
                    "pub_date": datetime(*entry.published_parsed[:6]),
                    "source_url": entry.link,
                }
                add_article_to_db(article)
                process_article.delay(article)
