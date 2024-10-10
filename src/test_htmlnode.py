import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):

    def test_props_to_html_multiple_props(self):
      node = HTMLNode(props={"href": "https://google.com", "target": "_blank"})
      self.assertEqual(node.props_to_html(), ' href="https://google.com" target="_blank"')

      
    def test_props_to_html_no_props(self):
      node = HTMLNode()
      self.assertEqual(node.props_to_html(), "")

      
    def test_props_to_html_single_prop(self):
      node = HTMLNode(props={"href": "https://google.com"})
      self.assertEqual(node.props_to_html(), ' href="https://google.com"')
       


if __name__ == "__main__":
    unittest.main()