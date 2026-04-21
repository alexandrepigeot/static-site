from enum import Enum

from leafnode import LeafNode


class TextType(Enum):
    TEXT = ""
    BOLD = "b"
    ITALIC = "i"
    CODE = "code"
    LINK = "a"
    IMAGE = "img"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

    def to_html_node(self, href="", src="", alt=""):
        match self.text_type:
            case TextType.TEXT:
                return LeafNode(tag=self.text_type.value, value=self.text)
            case TextType.BOLD:
                return LeafNode(tag=self.text_type.value, value=self.text)
            case TextType.ITALIC:
                return LeafNode(tag=self.text_type.value, value=self.text)
            case TextType.CODE:
                return LeafNode(tag=self.text_type.value, value=self.text)
            case TextType.LINK:
                return LeafNode(
                    tag=self.text_type.value,
                    value=self.text,
                    props={"href": href},
                )
            case TextType.IMAGE:
                return LeafNode(
                    tag=self.text_type.value, value="", props={"src": src, "alt": alt}
                )
            case _:
                raise Exception("Invalid text type")

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue
        
        split_node = node.text.split(delimiter)

        if (len(split_node) + 1) % 2 != 0:
            raise Exception(
                f"Missing closing delimiter '{delimiter}' in '{node.text}'")
        
        marking = False if split_node[0] else True
        
        for part in split_node:
            if part:
                if marking:
                    new_nodes.append(TextNode(text=part, text_type=text_type))
                else:
                    new_nodes.append(TextNode(text=part, text_type=TextType.TEXT))
                marking = not marking

    return new_nodes