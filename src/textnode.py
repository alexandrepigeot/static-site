from enum import Enum

from extract import extract_markdown_images, extract_markdown_links
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

def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue

        images = extract_markdown_images(node.text)

        if len(images) == 0:
            new_nodes.append(node)
            continue

        current_text = node.text

        for image in images:
            sections = current_text.split(f"![{image[0]}]({image[1]})", 1)

            new_nodes.append(TextNode(
                text=sections[0], text_type=TextType.TEXT
            ))

            new_nodes.append(TextNode(
                text=image[0], text_type=TextType.IMAGE, url=image[1]
            ))

            current_text = sections[1]
        
        if current_text:        
            new_nodes.append(TextNode(
                text=current_text, text_type=TextType.TEXT
            ))
    
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue
        
        links = extract_markdown_links(node.text)

        if len(links) == 0:
            new_nodes.append(node)
            continue
        
        current_text = node.text

        for link in links:
            sections = current_text.split(f"[{link[0]}]({link[1]})", 1)

            new_nodes.append(TextNode(
                text=sections[0], text_type=TextType.TEXT
            ))

            new_nodes.append(TextNode(
                text=link[0], text_type=TextType.LINK, url=link[1]
            ))

            current_text = sections[1]

        if current_text:
            new_nodes.append(TextNode(
                text=current_text, text_type=TextType.TEXT
            ))
        
    return new_nodes

def text_to_textnodes(text):
    nodes_list = split_nodes_delimiter(
        [TextNode(text=text, text_type=TextType.TEXT)],delimiter="**", text_type=TextType.BOLD
    )

    nodes_list = split_nodes_delimiter(
        nodes_list, delimiter="_", text_type=TextType.ITALIC
    )

    nodes_list = split_nodes_delimiter(
        nodes_list, delimiter="`", text_type=TextType.CODE
    )

    nodes_list = split_nodes_image(nodes_list)

    return split_nodes_link(nodes_list)
