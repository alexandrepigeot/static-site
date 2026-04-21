class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        result = ""

        if self.props is None:
            return result

        for prop in self.props:
            result += f' {prop}="{self.props[prop]}"'

        return result

    def __repr__(self):
        children_text = len(self.children) if self.children is not None else 0

        return f"HTMLNode(tag: {self.tag}, value: {self.value}, children: {children_text}, props: {self.props_to_html() if self.props is not None else None})"
