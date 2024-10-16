import unittest

from leafnode import LeafNode
from parentnode import ParentNode


class TestParentNode(unittest.TestCase):
  def test_parent_with_props(self):
    node = ParentNode("div", [LeafNode("p", "hello")], {"src": "./image.png"})
    self.assertEqual(node.to_html(), '<div src="./image.png"><p>hello</p></div>')
  
  
  def test_empty_children(self):
    node = ParentNode("div", [])
    with self.assertRaises(ValueError):
      node.to_html()
  
  
  def test_to_html(self):
    node = ParentNode(
      "div",
      children=[
        LeafNode("p", "im frog"),
        LeafNode(None, "normal txt"),
        LeafNode("i", "italic")
      ] 
    )
    self.assertEqual(node.to_html(), "<div><p>im frog</p>normal txt<i>italic</i></div>")

  
  def test_nested_parents(self):
    node = ParentNode("div", [
        LeafNode("p", "im frog"),
        ParentNode("div", [LeafNode(None, "g'day. only child")]),
        LeafNode("i", "italic")
    ])
    self.assertEqual(node.to_html(), "<div><p>im frog</p><div>g'day. only child</div><i>italic</i></div>")

    
  def test_no_children(self):
    node = ParentNode("p", None)
    with self.assertRaises(ValueError):
      node.to_html()

  def test_no_tag(self):
    node = ParentNode(None, [LeafNode("p", "frogs")])
    with self.assertRaises(ValueError):
      node.to_html()
    
      