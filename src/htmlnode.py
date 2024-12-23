class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
    def to_html(self) -> None:
        raise NotImplementedError
    
    def props_to_html(self) -> str:
        text = ""
        for key, val in self.props.items():
            text += f' {key}="{val}"'
        return text
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None) -> None:
        super().__init__(tag, value, None, props)
    
    def to_html(self) -> str:
        if self.tag == "img":
            if self.props is None or "src" not in self.props or "alt" not in self.props:
                raise ValueError
            props_str = self.props_to_html() if self.props else ""
            return f'<{self.tag}{props_str}/>'
        if self.value in [None, ""]:
            raise ValueError
        if self.tag is None:
            return f"{self.value}"
        props_str = self.props_to_html() if self.props else ""
        return f'<{self.tag}{props_str}>{self.value}</{self.tag}>'
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None) -> None:
        super().__init__(tag, None, children, props)

    def to_html(self) -> str:
        if not self.tag:
            raise ValueError("The parent node must have a valid tag")
        if not isinstance(self.children, list) or not self.children:
            raise ValueError("The parent node must have a non-empty list of children")
        value = "".join(child.to_html() for child in self.children)
        props_str = self.props_to_html() if self.props else ""
        return f'<{self.tag}{props_str}>{value}</{self.tag}>'


