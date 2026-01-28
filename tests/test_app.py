import unittest

class TestApp(unittest.TestCase):

    def test_app_import(self):
        import src.app  # noqa
        # If no exception, test passes
