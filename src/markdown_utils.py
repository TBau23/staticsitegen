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
    pattern = rf'({escaped_delimiter}.+?{escaped_delimiter})'
    segments = re.split(pattern, text)
    result = [
        {
            "content": segment.strip(delimiter),
            "is_delimited": segment.startswith(delimiter) and segment.endswith(delimiter)
        }
        for segment in segments if segment
    ]
    return result

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
        else:
            images = extract_markdown_images(node.text)
            segments = re.split(r'!\[(.*?)\]\((.*?)\)', node.text)
            img_idx = 0
            for s in segments:
                if s in images[img_idx]:
                    new_nodes.append(TextNode(s, TextType.IMAGE, images[img_idx][1]))
                    img_idx += 1
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
        else:
            links = extract_markdown_links(node.text)
            segments = re.split(r'\[(.*?)\]\((.*?)\)', node.text)
            link_idx = 0
            for s in segments:
                if s in links[link_idx]:
                    new_nodes.append(TextNode(s, TextType.LINK, links[link_idx][1]))
                    link_idx += 1
    return new_nodes

def extract_markdown_links(text):
    pattern = r'\[(.*?)\]\((.*?)\)'
    matches = re.findall(pattern, text)
    return matches

def extract_markdown_images(text):
    pattern = r'!\[(.*?)\]\((.*?)\)'
    matches = re.findall(pattern, text)
    return matches


node = TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", TextType.NORMAL)
split_nodes_image([node])

# extract_markdown_images("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)")
