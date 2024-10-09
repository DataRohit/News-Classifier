import unittest

from app.database import add_article_to_db


class TestDatabase(unittest.TestCase):
    def test_add_article(self):
        article = {
            "title": "Test Article",
            "content": "Content",
            "pub_date": "2024-10-09",
            "source_url": "http://example.com",
        }
        add_article_to_db(article)


if __name__ == "__main__":
    unittest.main()
