from celery import Celery

from app.classifier import classify_article
from app.database import Article, Session

celery = Celery(
    "tasks", backend="redis://localhost:6379/0", broker="redis://localhost:6379/0"
)


@celery.task
def process_article(article):
    session = Session()
    category = classify_article(article)
    db_article = session.query(Article).filter_by(title=article["title"]).first()
    if db_article:
        db_article.category = category
        session.commit()
    session.close()
