

class HTMLNode:
    def __init__(self, tag: str = None, value: str = None, children: list = None, props: dict = None):
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
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    