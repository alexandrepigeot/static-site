import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_default(self):
        node = LeafNode(tag="p", value="This is a leaf node")
        self.assertEqual(
            f"{node}", "LeafNode(tag: p, value: This is a leaf node, props: None)"
        )

    def test_with_props(self):
        node = LeafNode(
            tag="p",
            value="This is a leaf node",
            props={
                "href": "https://www.google.com",
                "rel": "stylesheet",
                "target": "_blank",
            },
        )

        self.assertEqual(
            f"{node}",
            'LeafNode(tag: p, value: This is a leaf node, props:  href="https://www.google.com" rel="stylesheet" target="_blank")',
        )

    def test_to_html(self):
        node = LeafNode(tag="p", value="This is a leaf node")
        self.assertEqual(node.to_html(), "<p>This is a leaf node</p>")

    def test_to_html_with_props(self):
        node = LeafNode(
            tag="p",
            value="This is a leaf node",
            props={
                "href": "https://www.google.com",
                "rel": "stylesheet",
                "target": "_blank",
            },
        )
        self.assertEqual(
            node.to_html(),
            '<p href="https://www.google.com" rel="stylesheet" target="_blank">This is a leaf node</p>',
        )
