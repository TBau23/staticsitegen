import unittest
from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplitNodesDelimiter(unittest.TestCase):
    def test1(self):
        input_nodes = [TextNode("This is text with a `code block` word", TextType.NORMAL)]
        result = split_nodes_delimiter(input_nodes, '`', TextType.CODE)
        print(result, 'RESULT')
        expected_result = [
            TextNode("This is text with a ", TextType.NORMAL, None),
            TextNode("code block", TextType.CODE, None),
            TextNode(" word", TextType.NORMAL, None)
        ]
        self.assertEqual(len(result), len(expected_result))
        self.assertEqual(result, expected_result)
