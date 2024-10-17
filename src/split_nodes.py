from extract_markdown import extract_markdown_images, extract_markdown_links
from textnode import TextNode
from enums import TextType


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        text = node.text
        extracted = extract_markdown_images(text)

        if not extracted:
            new_nodes.append(node)
            continue

        curr_pos = 0
        for alt_text, image_url in extracted:
            # get markdown from text
            markdown = f"![{alt_text}]({image_url})"
            start_index = text.find(markdown, curr_pos)

            # add text before markdown
            if start_index > curr_pos:
                pre_text = text[curr_pos:start_index]
                if pre_text:
                    new_nodes.append(TextNode(pre_text, TextType.TEXT))

            new_nodes.append(TextNode(alt_text, TextType.IMAGE, image_url))

            # update position after markdown
            curr_pos = start_index + len(markdown)

        # add leftover text after last markdown
        if curr_pos < len(text):
            new_nodes.append(TextNode(text[curr_pos:], TextType.TEXT))

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        text = node.text
        extracted = extract_markdown_links(text)

        if not extracted:
            new_nodes.append(node)
            continue

        curr_pos = 0
        for link_text, link_url in extracted:
            # get markdown from text
            markdown = f"[{link_text}]({link_url})"
            start_index = text.find(markdown, curr_pos)

            # add text before markdown
            if start_index > curr_pos:
                pre_text = text[curr_pos:start_index]
                if pre_text:
                    new_nodes.append(TextNode(pre_text, TextType.TEXT))

            new_nodes.append(TextNode(link_text, TextType.LINK, link_url))

            # update position after markdown
            curr_pos = start_index + len(markdown)

        # add leftover text after last markdown
        if curr_pos < len(text):
            new_nodes.append(TextNode(text[curr_pos:], TextType.TEXT))

    return new_nodes
