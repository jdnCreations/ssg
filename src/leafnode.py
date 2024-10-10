from htmlnode import HTMLNode


class LeafNode(HTMLNode):
  def __init__(self, tag=None, value=None, props=None):
    super().__init__(tag=tag, value=value, props=props, children=None)

  def to_html(self):
    if self.value is None:
      raise ValueError("LeafNode must have a value")
    if self.tag is None:
      return self.value
    if self.tag is "img":
      return f"<{self.tag}{self.props_to_html()}>"
    return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"