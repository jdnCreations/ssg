import re

def extract_markdown_links(text):
  markdown_links = []
  
  matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

  for match in matches:
      markdown_links.append(match)
  return markdown_links