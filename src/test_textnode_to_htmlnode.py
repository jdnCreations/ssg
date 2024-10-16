import unittest

from leafnode import LeafNode
from textnode import TextNode
from enums import TextType
from textnode_to_htmlnode import textnode_to_htmlnode


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text_type(self):
        node = TextNode("Hello", TextType.TEXT)
        self.assertEqual(textnode_to_htmlnode(node), LeafNode(None, "Hello"))

    def test_bold_type(self):
        node = TextNode("Hello", TextType.BOLD)
        self.assertEqual(textnode_to_htmlnode(node), LeafNode("b", "Hello"))

    def test_italic_type(self):
        node = TextNode("Hello", TextType.ITALIC)
        self.assertEqual(textnode_to_htmlnode(node), LeafNode("i", "Hello"))

    def test_code_type(self):
        node = TextNode("Hello", TextType.CODE)
        converted = textnode_to_htmlnode(node)
        self.assertEqual(converted, LeafNode("code", "Hello"))

    def test_link_type(self):
        node = TextNode("Hello", TextType.LINK, "https://google.com")
        converted = textnode_to_htmlnode(node)
        self.assertEqual(converted, LeafNode(
            "a", "Hello", {"href": "https://google.com"}))

    def test_image_type(self):
        node = TextNode("an image", TextType.IMAGE,
                        "https://imgur.com/dpfwerj")
        converted = textnode_to_htmlnode(node)
        self.assertEqual(converted, LeafNode(
            "img", "", {"src": "https://imgur.com/dpfwerj", "alt": "an image"}))
