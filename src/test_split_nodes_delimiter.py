import unittest
from split_nodes_delimiter import split_nodes_delimiter
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