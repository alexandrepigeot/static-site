import unittest

from leafnode import LeafNode
from textnode import TextNode, TextType, split_nodes_delimiter


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_with_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.google.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://www.google.com")
        self.assertEqual(node, node2)

    def test_diff_texts(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_diff_types(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.CODE)
        self.assertNotEqual(node, node2)

    def test_diff_urls(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.google.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://www.amazon.com")
        self.assertNotEqual(node, node2)

    def test_text_to_html(self):
        node = TextNode("This is a test node", TextType.TEXT)
        leaf = LeafNode(tag="", value="This is a test node")
        self.assertEqual(node.to_html_node().children, leaf.children)
        self.assertEqual(node.to_html_node().props, leaf.props)
        self.assertEqual(node.to_html_node().tag, leaf.tag)
        self.assertEqual(node.to_html_node().value, leaf.value)

    def test_bold_to_html(self):
        node = TextNode("This is a test node", TextType.BOLD)
        leaf = LeafNode(tag="b", value="This is a test node")
        self.assertEqual(node.to_html_node().children, leaf.children)
        self.assertEqual(node.to_html_node().props, leaf.props)
        self.assertEqual(node.to_html_node().tag, leaf.tag)
        self.assertEqual(node.to_html_node().value, leaf.value)

    def test_italic_to_html(self):
        node = TextNode("This is a test node", TextType.ITALIC)
        leaf = LeafNode(tag="i", value="This is a test node")
        self.assertEqual(node.to_html_node().children, leaf.children)
        self.assertEqual(node.to_html_node().props, leaf.props)
        self.assertEqual(node.to_html_node().tag, leaf.tag)
        self.assertEqual(node.to_html_node().value, leaf.value)

    def test_code_to_html(self):
        node = TextNode("This is a test node", TextType.CODE)
        leaf = LeafNode(tag="code", value="This is a test node")
        self.assertEqual(node.to_html_node().children, leaf.children)
        self.assertEqual(node.to_html_node().props, leaf.props)
        self.assertEqual(node.to_html_node().tag, leaf.tag)
        self.assertEqual(node.to_html_node().value, leaf.value)

    def test_link_to_html(self):
        node = TextNode("This is a test node", TextType.LINK)
        leaf = LeafNode(
            tag="a",
            value="This is a test node",
            props={"href": "https://www.google.com"},
        )
        self.assertEqual(
            node.to_html_node(href="https://www.google.com").children, leaf.children
        )
        self.assertEqual(
            node.to_html_node(href="https://www.google.com").props, leaf.props
        )
        self.assertEqual(node.to_html_node(href="https://www.google.com").tag, leaf.tag)
        self.assertEqual(
            node.to_html_node(href="https://www.google.com").value, leaf.value
        )

    def test_image_to_html(self):
        node = TextNode("This is a test node", TextType.IMAGE)
        leaf = LeafNode(
            tag="img",
            value="This is a test node",
            props={"src": "/imagesource.png", "alt": "Sourced image"},
        )
        self.assertEqual(
            node.to_html_node(src="/imagesource.png", alt="Sourced image").children,
            leaf.children,
        )
        self.assertEqual(
            node.to_html_node(src="/imagesource.png", alt="Sourced image").props,
            leaf.props,
        )
        self.assertEqual(
            node.to_html_node(src="/imagesource.png", alt="Sourced image").tag, leaf.tag
        )
        self.assertEqual(
            node.to_html_node(src="/imagesource.png", alt="Sourced image").value,
            "",
        )
    
    def test_split_plain_text(self):
        split_nodes = split_nodes_delimiter([
            TextNode(
                text="This one has a *BOLD* text", text_type=TextType.TEXT),
            TextNode(
                text="*This* one starts with bold", text_type=TextType.TEXT),
            TextNode(
                text="This one ends with *bold*", text_type=TextType.TEXT)
        ], "*", text_type=TextType.BOLD)

        self.assertEqual(split_nodes,[
            TextNode(text="This one has a ", text_type=TextType.TEXT),
            TextNode(text="BOLD", text_type=TextType.BOLD),
            TextNode(text=" text", text_type=TextType.TEXT),
            TextNode(text="This", text_type=TextType.BOLD),
            TextNode(text=" one starts with bold", text_type=TextType.TEXT),
            TextNode(text="This one ends with ", text_type=TextType.TEXT),
            TextNode(text="bold", text_type=TextType.BOLD)
        ])


if __name__ == "__main__":
    unittest.main()
