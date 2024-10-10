from htmlnode import HTMLNode


class ParentNode(HTMLNode):
  def __init__(self, tag, children, props=None):
    super().__init__(tag, children=children, props=props)
    
  def to_html(self):
    if self.tag is None:
      raise ValueError("ParentNode must have a tag")
    if not self.children:
      raise ValueError("ParentNode must have children")
    
    all_children = "".join([child.to_html() for child in self.children])
    return f"<{self.tag}{self.props_to_html()}>{all_children}</{self.tag}>"
    