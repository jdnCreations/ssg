import enum
from enums import TextType
from textnode import TextNode


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    if delimiter == "" or delimiter is None:
        raise ValueError("No delimiter supplied")
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT or delimiter not in node.text:
            new_nodes.append(node)
            continue
        delimiter_count = node.text.count(delimiter)
        if delimiter_count < 2:
            raise ValueError("Mismatched delimiters in the text")
        split_text = node.text.split(delimiter)
        for idx, text in enumerate(split_text):
            if text == "":
                continue
            curr_type = TextType.TEXT
            if idx == 1:
                curr_type = text_type
            node = TextNode(text, curr_type)
            new_nodes.append(node)

    return new_nodes
