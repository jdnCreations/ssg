from extract_markdown import extract_markdown_images
from split_nodes import split_nodes_image, split_nodes_link
from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextNode
from enums import TextType


def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(
        nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    return nodes
