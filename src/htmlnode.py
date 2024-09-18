class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        if self.props is None:
            return ""
        props_string = ""
        for prop in self.props:
            props_string +=f' {prop}="{self.props[prop]}"'
        return props_string

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"



class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("No value for LeafNode")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"





class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if not self.tag:
            raise ValueError("No tag for ParentNode")
        if not self.children:
            raise ValueError("No children for ParentNode")
        children_string = ""
        for child in self.children:
            children_string += child.to_html()
        return f'<{self.tag}{self.props_to_html()}>{children_string}</{self.tag}>'
            
        


        
    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"

test = LeafNode("b", "Bold text")
print(type(test))