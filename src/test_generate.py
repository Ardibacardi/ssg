import unittest
from generate import extract_title, generate_page

class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        md = "# Title"
        self.assertEqual(extract_title(md), "Title")

    def test_extract_title_no_title(self):
        md = "No title"
        self.assertRaises(Exception, extract_title, md)

        