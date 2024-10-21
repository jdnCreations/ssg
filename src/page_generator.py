from genericpath import isfile
import os
from pathlib import Path

from inline_markdown import extract_title
from markdown_to_blocks import markdown_to_html_node


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {
          dest_path} using {template_path}")

    with open(from_path) as file:
        content = file.read()

    with open(template_path) as file:
        template = file.read()

    html_node = markdown_to_html_node(content)
    html = html_node.to_html()
    split_lines = content.split("\n")
    title = extract_title(split_lines[0])
    new_file_data = template.replace(
        "{{ Title }}", title)
    new_file_data = new_file_data.replace("{{ Content }}", html)

    new_html_file_path = dest_path.replace('.md', '.html')

    with open(new_html_file_path, 'w') as file:
        file.write(new_file_data)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    # Crawl every entry in the content directory
    files_in_dir = os.listdir(dir_path_content)
    for file in files_in_dir:
        file_path = os.path.join(dir_path_content, file)
        print(file_path)
        if os.path.isfile(file_path):
            if file_path.endswith(".md"):
                base_filename = os.path.splitext(
                    os.path.basename(file_path))[0]
                new_html_file_path = os.path.join(
                    dest_dir_path, f"{base_filename}.html")
                os.makedirs(dest_dir_path, exist_ok=True)
                generate_page(file_path, template_path, new_html_file_path)

        if os.path.isdir(file_path):
            relative_path = os.path.relpath(file_path, dir_path_content)
            new_dest_dir_path = os.path.join(dest_dir_path, relative_path)
            os.makedirs(new_dest_dir_path, exist_ok=True)
            generate_pages_recursive(
                file_path, template_path, new_dest_dir_path)
