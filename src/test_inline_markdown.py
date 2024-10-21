import unittest

from inline_markdown import extract_markdown_images, extract_markdown_links, extract_title, split_nodes_delimiter, split_nodes_image, split_nodes_link, text_to_textnodes
from textnode import TextNode, TextType


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


class TestTextToTextNodes(unittest.TestCase):
    def test_text_to_textnodes(self):
        nodes = text_to_textnodes(
            "This is **text** with an *italic* word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)")
        self.assertEqual([
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE,
                     "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev")
        ],
            nodes)


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_delim_underscore(self):
        node = TextNode("This is text with a _italic_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertListEqual([
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word", TextType.TEXT)
        ], new_nodes)

    def test_delim_unclosed(self):
        node = TextNode("This is text with a italic_ word", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "_", TextType.ITALIC)

    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded word", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an *italic* word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and *italic*", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.ITALIC)
        self.assertEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )

    def test_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )


class TestExtractMarkdownImages(unittest.TestCase):
    def test_multiple_identical_images(self):
        text = "![alt](https://example.com/image.jpg) Some text ![alt](https://example.com/image.jpg)"
        expected = [("alt", "https://example.com/image.jpg"),
                    ("alt", "https://example.com/image.jpg")]
        self.assertEqual(extract_markdown_images(text), expected)

    def test_image_with_special_characters(self):
        text = "![image with spaces](https://example.com/image with spaces.jpg)"
        expected = [
            ("image with spaces", "https://example.com/image with spaces.jpg")]
        self.assertEqual(extract_markdown_images(text), expected)

    def test_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"

        self.assertEqual(extract_markdown_images(text), [
                         ("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])

    def test_extract_no_images(self):
        text = "This is text with no images"
        self.assertEqual(extract_markdown_images(text), [])

    def test_empty_alt_text(self):
        text = "![](https://example.com/image.jpg)"
        expected = [("", "https://example.com/image.jpg")]
        self.assertEqual(extract_markdown_images(text), expected)


class TestExtractMarkdownLinks(unittest.TestCase):
    def test_malformed_link(self):
        text = "[Broken link(https://example.com)"
        self.assertEqual(extract_markdown_links(text), [])

    def test_markdown_in_link_text(self):
        text = "[Link with **bold** and *italic*](https://example.com)"
        expected = [("Link with **bold** and *italic*", "https://example.com")]
        self.assertEqual(extract_markdown_links(text), expected)

    def test_link_within_image_alt_text(self):
        text = "![This is an image with a [link](https://example.com) in alt text](https://image.com/pic.jpg)"
        expected = [("link", "https://example.com")]
        self.assertEqual(extract_markdown_links(text), expected)

    def test_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"

        self.assertEqual(extract_markdown_links(text), [
                         ("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")])

    def test_extract_no_links(self):
        text = "This is text with no links"
        self.assertEqual(extract_markdown_links(text), [])


class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        text = "# Hello"
        extracted = extract_title(text)
        self.assertEqual(extracted, "Hello")

    def test_multiple_spaces(self):
        text = "#    Hello"
        extracted = extract_title(text)
        self.assertEqual(extracted, "Hello")
        text = "# Hello   "
        extracted = extract_title(text)
        self.assertEqual(extracted, "Hello")
        text = " # Hello "
        with self.assertRaisesRegex(Exception, "No h1 header."):
            extract_title(text)

    def test_empty_string(self):
        with self.assertRaisesRegex(Exception, "No h1 header."):
            extract_title("")

    def test_no_hash(self):
        with self.assertRaisesRegex(Exception, "No h1 header."):
            extract_title("Hello")
