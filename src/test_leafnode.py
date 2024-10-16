import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
  def test_no_value(self):
    with self.assertRaises(ValueError):
      node = LeafNode("p", None)
      

  def test_no_tag(self):
    node = LeafNode(tag=None, value="Paragraph")
    self.assertEqual(node.to_html(), "Paragraph")

  
  def test_proper_usage(self):
    node = LeafNode("p", "hello")
    self.assertEqual(node.to_html(), "<p>hello</p>")