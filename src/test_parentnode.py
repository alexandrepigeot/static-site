import unittest

from leafnode import LeafNode
from parentnode import ParentNode


class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        node = ParentNode(
            tag="div",
            children=[
                ParentNode(
                    tag="p",
                    children=[
                        LeafNode(tag=None, value="Some text "),
                        LeafNode(tag="i", value="italic"),
                    ],
                ),
                LeafNode(tag="p", value="Another paragraph maybe"),
            ],
            props={"autofocus": "True"},
        )
        self.assertEqual(
            node.to_html(),
            '<div autofocus="True"><p>Some text <i>italic</i></p><p>Another paragraph maybe</p></div>',
        )
