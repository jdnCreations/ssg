import unittest

from convert_nodes import text_node_to_html_node
from leafnode import LeafNode
from textnode import TextNode


class TestConvertNodes(unittest.TestCase):
  def test_for_text(self):
    text_node = TextNode("Hello", "text")
    leaf_node = text_node_to_html_node(text_node)
    self.assertEqual(leaf_node.to_html(), f"{text_node.text}")
    
  def test_for_bold(self):
    text_node = TextNode("Hello", "bold")
    leaf_node = text_node_to_html_node(text_node)
    self.assertEqual(leaf_node.to_html(), f"<b>{text_node.text}</b>")

    
  def test_for_italic(self):
    text_node = TextNode("Hello", "italic")
    leaf_node = text_node_to_html_node(text_node)
    self.assertEqual(leaf_node.to_html(), f"<i>{text_node.text}</i>")


  def test_for_code(self):
    text_node = TextNode("Hello", "code")
    leaf_node = text_node_to_html_node(text_node)
    self.assertEqual(leaf_node.to_html(), f"<code>{text_node.text}</code>")

    
  
  def test_for_link(self):
    text_node = TextNode("Hello", "link", "https://google.com")
    leaf_node = text_node_to_html_node(text_node)
    self.assertEqual(leaf_node.to_html(), f'<a href="{text_node.url}">{text_node.text}</a>')

  def test_for_image(self):
    text_node = TextNode("Hello", "image", "/image.png")
    leaf_node = text_node_to_html_node(text_node)
    self.assertEqual(leaf_node.to_html(), f'<img src="{text_node.url}" alt="{text_node.text}">')