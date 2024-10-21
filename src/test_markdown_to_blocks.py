import unittest

from markdown_to_blocks import block_to_block_type, markdown_to_blocks, block_type_code, block_type_heading, block_type_olist, block_type_ulist, block_type_quote, block_type_paragraph, markdown_to_html_node


class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html, "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>")

    def test_heading(self):
        md = """
### Heading Text goes absolutely *brazy* am i right?

yes you are right
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html, "<div><h3>Heading Text goes absolutely <i>brazy</i> am i right?</h3><p>yes you are right</p></div>")


class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""

        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks,
                         [
                             "This is **bolded** paragraph",
                             "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                             "* This is a list\n* with items"
                         ])


class TestBlockToBlockType(unittest.TestCase):
    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), block_type_heading)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), block_type_code)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), block_type_quote)
        block = "* list\n* items"
        self.assertEqual(block_to_block_type(block), block_type_ulist)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), block_type_olist)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)

    def test_incorrect_code(self):
        block = """```code i guess``"""
        self.assertEqual(block_to_block_type(block), block_type_paragraph)

    def test_multiline_code(self):
        block = "```code\non\n multiple\nlines```"
        self.assertEqual(block_to_block_type(block), block_type_code)
