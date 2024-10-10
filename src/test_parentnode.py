from lib2to3.pytree import Leaf
import unittest

from leafnode import LeafNode
from parentnode import ParentNode

class TestParentNode(unittest.TestCase):
  def test_multiple_leafnode_children(self):
    node = ParentNode("div", children=[LeafNode("p", "im a child"), LeafNode("p", "another child")])
    self.assertEqual(node.to_html(), "<div><p>im a child</p><p>another child</p></div>")

    
  def test_multiple_parentnode_children(self):
    node = ParentNode("div", children=[ParentNode("div", children=[LeafNode(value="frog")]), ParentNode("div", children=[LeafNode(value="froggies")])])
    self.assertEqual(node.to_html(), "<div><div>frog</div><div>froggies</div></div>")

    
  # tests if having leafnodes and parentnodes as children works
  def test_leafnode_parentnode_children(self):
    node = ParentNode(
      "div", children=[ParentNode("div", children=[LeafNode(value="Hey im a leaf")]), LeafNode(value="leaf")])
    self.assertEqual(node.to_html(), "<div><div>Hey im a leaf</div>leaf</div>")

  def test_parentnode_properties(self):
    node = ParentNode("div", children=[LeafNode(value="Leafnode moment")], props={"href": "https://google.com"})
    self.assertEqual(node.to_html(), '<div href="https://google.com">Leafnode moment</div>')

    
  def test_parentnode_no_tag(self):
    node = ParentNode(tag=None, children=[LeafNode(value="hey")])
    with self.assertRaises(ValueError):
      node.to_html() 

  def test_parentnode_no_children(self):
    node = ParentNode(tag="div", children=None)
    with self.assertRaises(ValueError):
      node.to_html()