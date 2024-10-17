from math import exp
import unittest

from text_to_textnodes import text_to_textnodes
from textnode import TextNode
from enums import TextType


class TestTextToTextNodes(unittest.TestCase):
    def test_all_in_one(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        new_nodes = text_to_textnodes(text)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE,
                     "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertEqual(new_nodes, expected)

    def test_text(self):
        nodes = text_to_textnodes("Hello World")
        expected = [TextNode("Hello World", TextType.TEXT)]
        self.assertEqual(nodes, expected)

    def test_with_delimiter(self):
        nodes = text_to_textnodes("*Hello* World")
        expected = [TextNode("Hello", TextType.ITALIC),
                    TextNode(" World", TextType.TEXT)]
        self.assertEqual(nodes, expected)

    def test_with_bold_delimiter(self):
        nodes = text_to_textnodes("**Hello** World")
        expected = [TextNode("Hello", TextType.BOLD),
                    TextNode(" World", TextType.TEXT)]
        self.assertEqual(nodes, expected)

    def test_with_code_delimiter(self):
        nodes = text_to_textnodes("`Hello` World")
        expected = [TextNode("Hello", TextType.CODE),
                    TextNode(" World", TextType.TEXT)]
        self.assertEqual(nodes, expected)

    def test_with_multiple_delimiters(self):
        nodes = text_to_textnodes("**BOLD** *italic*.")
        expected = [
            TextNode("BOLD", TextType.BOLD),
            TextNode(" ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(".", TextType.TEXT)
        ]
        self.assertEqual(nodes, expected)

    def test_code_mid_text(self):
        nodes = text_to_textnodes("welcome to chil`lis` may I take your order")
        expected = [
            TextNode("welcome to chil", TextType.TEXT),
            TextNode("lis", TextType.CODE),
            TextNode(" may I take your order", TextType.TEXT)
        ]
        self.assertEqual(nodes, expected)

    def test_mismatched_delimiters(self):
        with self.assertRaisesRegex(ValueError, "Mismatched delimiters in the text"):
            nodes = text_to_textnodes("welcome to *chilis`")
