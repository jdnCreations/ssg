import unittest

from htmlnode import LeafNode
from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node2", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.TEXT,
                        "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.TEXT,
                         "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT,
                        "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text_type(self):
        node = TextNode("Hello", TextType.TEXT)
        self.assertEqual(text_node_to_html_node(node), LeafNode(None, "Hello"))

    def test_bold_type(self):
        node = TextNode("Hello", TextType.BOLD)
        self.assertEqual(text_node_to_html_node(node), LeafNode("b", "Hello"))

    def test_italic_type(self):
        node = TextNode("Hello", TextType.ITALIC)
        self.assertEqual(text_node_to_html_node(node), LeafNode("i", "Hello"))

    def test_code_type(self):
        node = TextNode("Hello", TextType.CODE)
        converted = text_node_to_html_node(node)
        self.assertEqual(converted, LeafNode("code", "Hello"))

    def test_link_type(self):
        node = TextNode("Hello", TextType.LINK, "https://google.com")
        converted = text_node_to_html_node(node)
        self.assertEqual(converted, LeafNode(
            "a", "Hello", {"href": "https://google.com"}))

    def test_image_type(self):
        node = TextNode("an image", TextType.IMAGE,
                        "https://imgur.com/dpfwerj")
        converted = text_node_to_html_node(node)
        self.assertEqual(converted, LeafNode(
            "img", "", {"src": "https://imgur.com/dpfwerj", "alt": "an image"}))
