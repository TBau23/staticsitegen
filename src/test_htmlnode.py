import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_create_node(self):
        node = HTMLNode("h1", "Hello", [], {})
        self.assertEqual(node.tag, "h1")
        self.assertEqual(node.value, "Hello")
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {})

    def test_create_with_props(self):
        node = HTMLNode("h1", "Hello", [], {"class": "test"})
        self.assertEqual(node.tag, "h1")
        self.assertEqual(node.value, "Hello")
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {"class": "test"})

    def test_props_to_html(self):
        node = HTMLNode("h1", "Hello", [], {"class": "test", "id": "testid"})
        self.assertEqual(node.props_to_html(), ' class="test" id="testid"')

    def test_repr(self):
        node = HTMLNode("h1", "Hello", [], {"class": "test", "id": "testid"})
        self.assertEqual(repr(node), '<h1 class="test" id="testid">Hello</h1>')

    