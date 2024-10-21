from genericpath import isfile
import os
import shutil
from page_generator import generate_page, generate_pages_recursive
from textnode import TextNode


def source_to_destination():

    # delete all contents of destination folder
    if os.path.exists("public"):
        print("PUBLIC EXISTS!")
        files = os.listdir("public")
        for file in files:
            file_path = os.path.join("public", file)
            if os.path.isfile(file_path):
                print(f"removing file {file_path}")
                os.remove(file_path)
            else:
                print(f"removing folder {file_path}")
                shutil.rmtree(file_path)
    # create public directory if it doesnt exist
    else:
        os.mkdir("public")

    # copy all contents inside source directory to destination directory
    if os.path.exists("static"):
        copyfiles("static", "public")


def copyfiles(from_location, to_location):
    files = os.listdir(from_location)
    for file in files:
        file_string = os.path.join(from_location, file)
        dest_file_string = os.path.join(to_location, file)
        if os.path.isfile(file_string):
            os.makedirs(os.path.dirname(dest_file_string), exist_ok=True)
            shutil.copyfile(file_string, dest_file_string)
        else:
            os.makedirs(dest_file_string, exist_ok=True)
            copyfiles(file_string, dest_file_string)
        print(f"copied file {file_string}")


def main():
    source_to_destination()
    generate_pages_recursive("content", "template.html", "public")


main()
