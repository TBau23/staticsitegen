import unittest
from markdown_utils import split_nodes_delimiter, extract_markdown_images, split_nodes_link, extract_markdown_links, split_nodes_image
from textnode import TextNode, TextType

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_simple_code_block(self):
        input_nodes = [TextNode("This is text with a `code block` word", TextType.NORMAL)]
        result = split_nodes_delimiter(input_nodes, '`', TextType.CODE)
        expected_result = [
            TextNode("This is text with a ", TextType.NORMAL, None),
            TextNode("code block", TextType.CODE, None),
            TextNode(" word", TextType.NORMAL, None)
        ]
        self.assertEqual(result, expected_result)

    def test_no_delimiter(self):
        input_nodes = [TextNode("This is text with a `code block word", TextType.NORMAL)]
        result = split_nodes_delimiter(input_nodes, '`', TextType.CODE)
        expected_result = [TextNode("This is text with a `code block word", TextType.NORMAL)]
        self.assertEqual(result, expected_result)

    def test_reoccurring_delimiter(self):
        input_nodes = [TextNode("Yo this is actually *italic* and also *again*", TextType.NORMAL)]
        result = split_nodes_delimiter(input_nodes, '*', TextType.ITALIC)
        expected_result = [
            TextNode("Yo this is actually ", TextType.NORMAL, None),
            TextNode("italic", TextType.ITALIC, None),
            TextNode(" and also ", TextType.NORMAL, None),
            TextNode("again", TextType.ITALIC, None),
        ]
        self.assertEqual(result, expected_result)

class TestExtractMarkdownImages(unittest.TestCase):
    def test_extract_markdown_images(self):
        input_text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        result = extract_markdown_images(input_text)
        expected_result = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(result, expected_result)

    def test_no_markdown_images(self):
        input_text = "This is text with no markdown images"
        result = extract_markdown_images(input_text)
        expected_result = []
        self.assertEqual(result, expected_result)
    
    def test_bad_markdown(self):
        input_text = "This is text with a !rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg"
        result = extract_markdown_images(input_text)
        expected_result = []
        self.assertEqual(result, expected_result)

class TextSplitNodesLink(unittest.TestCase):
    def test_simple_link(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_link([node])
        print('NEW_NODES!!',new_nodes)
        expected_result = [
            TextNode("This is text with a link ", TextType.NORMAL, None),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.NORMAL, None),
            TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
        ]
        print('EXPECTED_RESULT!!', expected_result)
        self.assertEqual(new_nodes, expected_result)

class TextSplitNodesImage(unittest.TestCase):
    pass