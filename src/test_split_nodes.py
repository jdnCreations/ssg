import unittest

from split_nodes import split_nodes_delimiter
from textnode import TextNode


class TestSplitNodes(unittest.TestCase):
  def test_one_delimiter_pair(self):
     node = TextNode("This is text with a `code block` word", "text")
     new_nodes = split_nodes_delimiter([node], "`", "code")
     
     # check the number of nodes is 3
     self.assertEqual(len(new_nodes), 3)
     self.assertEqual(new_nodes[0].text, "This is text with a ")
     self.assertEqual(new_nodes[0].text_type, "text")
     self.assertEqual(new_nodes[1].text, "code block")
     self.assertEqual(new_nodes[1].text_type, "code")
     self.assertEqual(new_nodes[2].text," word")
     self.assertEqual(new_nodes[2].text_type, "text")

     
  def test_multiple_delimiter_pairs(self):
    node = TextNode("This is text with `multiple` delimiter `pairs`", "text")
    new_nodes = split_nodes_delimiter([node], "`", "code")

    self.assertEqual(len(new_nodes), 4)
    self.assertEqual(new_nodes[0].text, "This is text with ")
    self.assertEqual(new_nodes[0].text_type, "text")
    self.assertEqual(new_nodes[1].text_type, "code")
    self.assertEqual(new_nodes[2].text_type, "text")
    self.assertEqual(new_nodes[3].text_type, "code")

    
  def test_single_delimiter(self):
    node = TextNode("Single `delimiter mentioned", "text")
    
    with self.assertRaises(Exception):
      new_nodes = split_nodes_delimiter([node], "`", "code")
      
    
  def test_mixed_types(self):
    nodes = [
      TextNode("Regular text.", "text"),
      TextNode("Bold text", "bold"),
      TextNode(" More regular text with a `code block` inside.", "text")
    ]
    new_nodes = split_nodes_delimiter(nodes, "`", "code")
    
    self.assertEqual(len(new_nodes), 5)
    self.assertEqual(new_nodes[0].text_type, "text")
    self.assertEqual(new_nodes[0].text, "Regular text.")
    self.assertEqual(new_nodes[1].text, "Bold text")
    self.assertEqual(new_nodes[1].text_type, "bold")
    self.assertEqual(new_nodes[2].text, " More regular text with a ")
    self.assertEqual(new_nodes[2].text_type, "text")
    self.assertEqual(new_nodes[3].text, "code block")
    self.assertEqual(new_nodes[3].text_type, "code")
    self.assertEqual(new_nodes[4].text, " inside.")
    self.assertEqual(new_nodes[4].text_type, "text")