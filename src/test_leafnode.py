import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_empty_tag(self):
        node = LeafNode(None, "Hello", {})
        self.assertEqual(node.to_html(), "Hello")

    def test_empty_value(self):
        node = LeafNode("h1", None, {})
        self.assertRaises(ValueError, node.to_html)
    
    def test_to_html(self):
        node = LeafNode("h1", "Hello", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<h1 href="https://www.google.com">Hello</h1>')
    
