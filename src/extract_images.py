import re

def extract_markdown_images(text):

  markdown_images = []
  
  matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
  
  for match in matches:
      markdown_images.append(match)

  return markdown_images

