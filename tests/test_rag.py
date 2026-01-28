import unittest
from unittest.mock import patch
from src.rag import ingest_pdf, rag_search, has_document


class TestRAG(unittest.TestCase):

    def test_ingest_empty(self):
        result = ingest_pdf(b"", "thread123")
        self.assertFalse(result["success"])

    @patch("src.rag._vectorstore")
    def test_rag_no_document(self, m_vs):
        m_vs.return_value = None
        out = rag_search("test", "thread123")
        self.assertIn("No document", out)

    @patch("src.rag._vectorstore")
    def test_rag_with_mock_hits(self, m_vs):
        class MockVS:
            def similarity_search(self, query, k=4):
                return [{"page_content": "Mocked content", "metadata": {"page": 2}}]

        m_vs.return_value = MockVS()
        out = rag_search("test", "thread123")
        self.assertIn("[rag_search]", out)
        self.assertIn("Mocked content", out)
