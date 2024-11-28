from textnode import TextNode, TextType

def main():
    res = TextNode('First node', TextType.BOLD, 'https://www.google.com')
    print(res)

main()