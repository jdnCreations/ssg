import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
  def test_no_value(self):
    node = LeafNode(value=None)
    with self.assertRaises(ValueError):
      node.to_html() 

  
  def test_no_tag(self):
    node = LeafNode(tag=None, props=None, value="Frogs!")
    self.assertEqual(node.to_html(), "Frogs!")

    
  def test_render_html_tag(self):
    node = LeafNode("p", "This is a paragraph")
    self.assertEqual(node.to_html(), "<p>This is a paragraph</p>")