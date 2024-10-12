import unittest

from extract_images import extract_markdown_images

class TestExtractImages(unittest.TestCase):
  def test_extract_images(self):
    text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    extracted = extract_markdown_images(text)
    
    self.assertEqual(extracted, [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])

  def test_extract_empty(self):
    text = ""
    
    extracted = extract_markdown_images(text)
    self.assertEqual(extracted, [])

      
  def test_extract_no_image(self):
    text = "This is a test with no image"
    extracted = extract_markdown_images(text)
    
    self.assertEqual(extracted, [])

      
  def test_single_image(self):
    text = "This is a test with one image ![clorbin](https://i.imgur.com/aKaOqIh.gif)"
    extracted = extract_markdown_images(text)
    self.assertEqual(extracted, [("clorbin", "https://i.imgur.com/aKaOqIh.gif")])

    
  def test_broken_markdown(self):
    text = "Test with broken markdown [clorbin](https://mgsr.com/"
    extracted = extract_markdown_images(text)
    
    self.assertEqual(extracted, [])

    
  def test_ignore_links(self):
    text = "This is a [link](https://example.com) and ![image](https://example.com/image.jpg)"
    extracted = extract_markdown_images(text)
    self.assertEqual(extracted, [("image", "https://example.com/image.jpg")])
    
    
      
  