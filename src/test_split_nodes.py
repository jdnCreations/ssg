import unittest

from extract_markdown import extract_markdown_links
from split_nodes import split_nodes_image, split_nodes_link
from textnode import TextNode
from enums import TextType


class TestSplitNodesLink(unittest.TestCase):
    def test_multiple_markdowns(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdev)", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertEqual(new_nodes, [
            TextNode(
                "This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("to youtube", TextType.LINK,
                     "https://www.youtube.com/@bootdev")
        ])

    def test_no_markdown(self):
        node = TextNode("This is text with a link", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertEqual(new_nodes, [node])


class TestSplitNodesImage(unittest.TestCase):
    def test_multiple_markdowns(self):
        node = TextNode(
            "Here is an image of a panda ![panda](https://example.com/panda.jpg) and a bear ![bear](https://example.com/bear.jpg)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        expected = [
            TextNode("Here is an image of a panda ", TextType.TEXT),
            TextNode("panda", TextType.IMAGE, "https://example.com/panda.jpg"),
            TextNode(" and a bear ", TextType.TEXT),
            TextNode("bear", TextType.IMAGE, "https://example.com/bear.jpg"),
        ]
        self.assertEqual(new_nodes, expected)

    def test_no_markdown(self):
        node = TextNode("Image of a panda and a bear", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertEqual(new_nodes, [node])
