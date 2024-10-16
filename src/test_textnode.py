import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold", "https://boot.dev")
        node2 = TextNode("This is a text node", "bold", "https://boot.dev")
        self.assertEqual(node, node2)

    def test_different_urls(self):
        node1 = TextNode("Text node", "text", "https://google.com")
        node2 = TextNode("Text node", "text", "https://boot.dev")
        self.assertNotEqual(node1, node2)

    def test_url(self):
        node = TextNode("Text node", "text", "https://google.com")
        self.assertEqual(node.url, "https://google.com")

    def test_text(self):
        node = TextNode("Text", "text")
        self.assertEqual(node.text, "Text")

    def test_text_type(self):
        node = TextNode("Text", "link")
        self.assertEqual(node.text_type, "link")
    

    def test_no_url(self):
        node = TextNode("Text", "text")
        self.assertIsNone(node.url)

    def test_diff_text(self):
        node1 = TextNode("Text1", "text")
        node2 = TextNode("Text2", "text")
        self.assertNotEqual(node1, node2)

    def test_withurl_without(self):
        node1 = TextNode("Text", "text", "https://boot.dev")
        node2 = TextNode("Text", "text")
        self.assertNotEqual(node1, node2)

      

if __name__ == "__main__":
    unittest.main()