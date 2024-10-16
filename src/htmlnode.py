class HTMLNode():
  def __init__(self, tag=None, value=None, children=None, props=None):
    self.tag = tag
    self.value = value
    self.children = children
    self.props = props

    
  def __repr__(self):
     return f"tag:{self.tag}, value:{self.value}, children:{self.children}, props:{self.props}"
    
    
  def to_html(self):
    raise NotImplementedError
  
  
  def props_to_html(self):
    if self.props == None:
      return ""

    if not isinstance(self.props, dict): 
      return ""
    stringified_props = ""

    for key in self.props:
      stringified_props += f' {key}="{self.props[key]}"'

    return stringified_props
    