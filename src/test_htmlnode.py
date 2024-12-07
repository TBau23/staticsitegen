import unittest
from htmlnode import HTMLNode, ParentNode, LeafNode

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
    
    def test_empty_props_to_html(self):
        node = HTMLNode("h1", "Hello", [], {})
        self.assertEqual(node.props_to_html(), '')

    def test_empty_repr(self):
        node = HTMLNode()
        self.assertEqual(repr(node), 'HTMLNode(None, None, children=None, {})')

    def test_repr(self):
        node = HTMLNode("h1", "Hello", [], {"class": "test", "id": "testid"})
        self.assertEqual(repr(node), "HTMLNode(h1, Hello, children=[], {'class': 'test', 'id': 'testid'})")

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

class TestParentNode(unittest.TestCase):
    def test_create_node(self):
        children = [LeafNode("h1", "Hello", {"href": "https://www.google.com"})]
        node = ParentNode("h1", children, {})
        self.assertEqual(node.tag, "h1")
        self.assertEqual(node.children, children)
        self.assertEqual(node.props, {})