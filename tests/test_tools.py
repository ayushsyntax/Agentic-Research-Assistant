import unittest
from unittest.mock import patch
from src.tools import web_search, get_stock_price


class TestTools(unittest.TestCase):

    @patch("src.tools.requests.post")
    @patch("src.tools.requests.get")
    def test_web_search_mocked(self, m_get, m_post):
        # Mock Serper returns sample result
        m_post.return_value.json.return_value = {
            "organic": [
                {"title": "Test", "snippet": "Snippet", "link": "https://example.com"}
            ]
        }
        out = web_search("test query")
        self.assertIn("[web_search]", out)
        self.assertIn("Test", out)

    @patch("src.tools.requests.get")
    def test_stock_mocked(self, m_get):
        m_get.return_value.json.return_value = {
            "Global Quote": {
                "05. price": "123.45",
                "10. change percent": "2.5%"
            }
        }
        out = get_stock_price("AAPL")
        self.assertIn("[get_stock_price]", out)
        self.assertIn("123.45", out)
