import unittest

from extract_markdown import extract_markdown_images, extract_markdown_links


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
