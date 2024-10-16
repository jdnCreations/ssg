import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
  def test_props_to_html(self):
    node = HTMLNode("p", "paragraph", None, {"src": "sauce", "href": "https://google.com"})
    self.assertEqual(node.props_to_html(), ' src="sauce" href="https://google.com"')

    
  def test_no_props(self):
    node = HTMLNode("div", "deeeeeiv", None, None)
    self.assertEqual(node.props_to_html(), "")

    
  def test_incorrect_props(self):
    node = HTMLNode("div", "dis a div", None, {2, 5})
    self.assertEqual(node.props_to_html(), "")


  def test_props_as_list(self):
    node = HTMLNode("div", "a diva is a female version of a hustler", None, ["frogs", "ribbit"])
    self.assertEqual(node.props_to_html(), "")