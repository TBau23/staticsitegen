import unittest
from htmlnode import LeafNode
from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_str(self):
        node = TextNode("This is a text node", TextType.BOLD)
        r = repr(node)
        self.assertEqual(r, "TextNode(This is a text node, bold, None)")
    
    def test_unequal_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)
    
    def test_unequal_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
    
    def test_unequal_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.google.com")
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_create_node(self):
        node = TextNode("test node", TextType.ITALIC, "https://www.google.com")
        self.assertEqual(node.text, 'test node')
        self.assertEqual(node.text_type, TextType.ITALIC)
        self.assertEqual(node.url, "https://www.google.com")


class TestTextNodeToHtmlNode(unittest.TestCase):

    def test_to_html_node_italic(self):
        node = TextNode("test node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node, LeafNode('i', 'test node'))

    def test_to_html_node_code(self):
        node = TextNode('wawacode', TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node, LeafNode('code', 'wawacode'))
    
    def test_to_html_node_link(self):
        node = TextNode('wawacode', TextType.LINK, 'https://www.google.com')
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node, LeafNode('a', 'wawacode', {'href': 'https://www.google.com'}))


if __name__ == "__main__":
    unittest.main()