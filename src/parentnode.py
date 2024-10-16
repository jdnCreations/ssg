

from htmlnode import HTMLNode


class ParentNode(HTMLNode):
  def __init__(self, tag, children, props=None):
    super().__init__(tag=tag, children=children, props=props)
    
  def to_html(self):
    if self.tag == None:
      raise ValueError("Must supply a tag")
    if self.children is None or len(self.children) == 0:
      raise ValueError("Must have children")
    htmlified = ""
    
    for child in self.children:
      htmlified += child.to_html() 

    return f"<{self.tag}{self.props_to_html()}>{htmlified}</{self.tag}>"