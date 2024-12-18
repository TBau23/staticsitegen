import re
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
        elif node.text_type == TextType.NORMAL:
            segments = create_delimited_segments(node.text, delimiter)
            for segment in segments:
                if segment["is_delimited"]:
                    new_nodes.append(TextNode(segment["content"], text_type))
                else:
                    new_nodes.append(TextNode(segment["content"], TextType.NORMAL))
    return new_nodes
    
def create_delimited_segments(text, delimiter):
    escaped_delimiter = re.escape(delimiter) #escape the delimiter so we can use it in regex safely
    pattern = rf'({escaped_delimiter}.*?{escaped_delimiter})'
    segments = re.split(pattern, text)
    print(segments, 'SEGMENTS')
    result = [
        {
            "content": segment.strip(delimiter),
            "is_delimited": segment.startswith(delimiter) and segment.endswith(delimiter)
        }
        for segment in segments if segment
    ]
    return result

                

n1 = TextNode('yo *yo* yo',TextType.ITALIC)

print(split_nodes_delimiter([TextNode("This is text with a `code block` word", TextType.NORMAL)], '`', TextType.CODE))