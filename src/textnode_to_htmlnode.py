from leafnode import LeafNode
from enums import TextType


def textnode_to_htmlnode(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            url = text_node.url if text_node.url else "default url"
            return LeafNode("a", text_node.text, {"href": url})
        case TextType.IMAGE:
            url = text_node.url if text_node.url else "default url"
            return LeafNode("img", "", {"src": url, "alt": text_node.text})
        case _:
            raise Exception("Incorrect TextType")
