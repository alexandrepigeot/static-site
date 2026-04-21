import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_default(self):
        node = HTMLNode()
        self.assertEqual(
            f"{node}", "HTMLNode(tag: None, value: None, children: 0, props: None)"
        )

    def test_with_tag(self):
        node = HTMLNode(tag="p")
        self.assertEqual(
            f"{node}", "HTMLNode(tag: p, value: None, children: 0, props: None)"
        )

    def test_with_value(self):
        node = HTMLNode(value="This is a test value")
        self.assertEqual(
            f"{node}",
            "HTMLNode(tag: None, value: This is a test value, children: 0, props: None)",
        )

    def test_with_children(self):
        node = HTMLNode(children=[HTMLNode(), HTMLNode(), HTMLNode()])
        self.assertEqual(
            f"{node}", "HTMLNode(tag: None, value: None, children: 3, props: None)"
        )

    def test_with_props(self):
        node = HTMLNode(
            props={
                "href": "https://www.google.com",
                "rel": "stylesheet",
                "target": "_blank",
            }
        )
        self.assertEqual(
            f"{node}",
            'HTMLNode(tag: None, value: None, children: 0, props:  href="https://www.google.com" rel="stylesheet" target="_blank")',
        )
