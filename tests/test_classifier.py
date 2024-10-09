import unittest

from app.classifier import classify_article


class TestClassifier(unittest.TestCase):
    def test_classify_article(self):
        article = {"content": "This is a happy article about success."}
        category = classify_article(article)
        self.assertIn(category, ["Positive/Uplifting", "Others"])


if __name__ == "__main__":
    unittest.main()
