from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self is None:
            return ""
        if self.tag is None:
            raise ValueError("all parent nodes must have a tag")
        if self.children is None:
            raise ValueError("all parent nodes must have children")
        
        str = ""
        for child in self.children: 
            str += child.to_html()
        return f'<{self.tag}>{str}</{self.tag}>'
        
    
    def __repr__(self):
        return f"Parent Node({self.tag}, children: {self.children}, {self.props})"
