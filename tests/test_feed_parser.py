import unittest

from app.feed_parser import parse_feeds


class TestFeedParser(unittest.TestCase):
    def test_parse_feeds(self):
        parse_feeds()


if __name__ == "__main__":
    unittest.main()
