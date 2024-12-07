

class HTMLNode:
    def __init__(self, tag: str = None, value: str = None, children: list = None, props: dict = {}):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
    def to_html(self):
        raise NotImplementedError("to_html not implemented")
    
    def props_to_html(self):
        html = ""
        for k, v in self.props.items():
            html += f' {k}="{v}"'
        return html
    
    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, children={self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag: str = None, value: str = '', props: dict = {}):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list, props: dict = {}):
        super().__init__(tag, children, props)
        
    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode requires a tag")
        elif len(self.children) == 0:
            raise ValueError("ParentNode requires children")
        else:
            html_children = ""
            for child in self.children:
                continue
