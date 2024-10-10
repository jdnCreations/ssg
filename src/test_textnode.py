import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_test_value(self):
        node = TextNode("This is a text node", "bold")
        self.assertEqual(node.text, "This is a text node")


    def test_url_none(self):
        node = TextNode("Text Node", "bold")
        self.assertEqual(node.url, None)


    def test_text_type_diff(self):
        node1 = TextNode("Txt Node", "bold")
        node2 = TextNode("Txt Node", "italic")
        self.assertNotEqual(node1.text_type, node2.text_type)


    def test_object_diff(self):
        node1 = TextNode("Txt Node", "bold")
        node2 = TextNode("Txt Node", "italic")
        self.assertNotEqual(node1, node2)


if __name__ == "__main__":
    unittest.main()