import unittest
from src.graph import chatbot


class TestGraph(unittest.TestCase):

    def test_graph_has_nodes(self):
        # minimal sanity check
        self.assertTrue(hasattr(chatbot, "stream"))
        self.assertTrue(hasattr(chatbot, "invoke"))
