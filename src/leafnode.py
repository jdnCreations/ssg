from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if value == None:
            raise ValueError
        super().__init__(tag, value, props)

    def __eq__(other, self):
        if not isinstance(other, LeafNode):
            return False
        return (self.tag == other.tag and
                self.value == other.value and
                self.props == other.props)

    def to_html(self):
        if self.tag == None:
            return self.value
        return f"<{self.tag}>{self.value}</{self.tag}>"
