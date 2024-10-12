import unittest

from extract_links import extract_markdown_links

class TestExtractLinks(unittest.TestCase):
  def test_extract_links(self):
    text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    extracted = extract_markdown_links(text)
    
    self.assertEqual(extracted, [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")])
  
  def test_extract_empty(self):
        text = ""
        extracted = extract_markdown_links(text)
        self.assertEqual(extracted, [])

  def test_extract_no_link(self):
        text = "This is a test with no link"
        extracted = extract_markdown_links(text)
        
        self.assertEqual(extracted, [])

  def test_single_link(self):
        text = "This is a test with one link [boot.dev](https://www.boot.dev)"
        extracted = extract_markdown_links(text)
        self.assertEqual(extracted, [("boot.dev", "https://www.boot.dev")])

  def test_broken_markdown(self):
        text = "Test with broken markdown [boot.dev](https://www.boot.dev/"
        extracted = extract_markdown_links(text)
        
        self.assertEqual(extracted, [])

  def test_ignore_images(self):
        text = "This is a [link](https://example.com) and ![image](https://example.com/image.jpg)"
        extracted = extract_markdown_links(text)
        self.assertEqual(extracted, [("link", "https://example.com")])