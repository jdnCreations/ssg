import os
from textnode import TextNode


def source_to_static():
    # delete all contents of destination folder
    if os.path.exists("public"):
        print("PUBLIC EXISTS!")
        files = os.listdir("public")
        for file in files:
            os.remove("public/" + file)
    else:
        os.mkdir("public")


def main():
    source_to_static()


main()
