import os
import shutil
from block_to_html import *


template = "template.html"


def static_to_public(source, destination, is_first_call=False):
    if is_first_call:
        shutil.rmtree(destination)
        os.mkdir(destination)
    file_list = os.listdir(source)
    for file in file_list:
        new_destination = os.path.join(destination, file)
        new_file = os.path.join(source, file)
        if os.path.isdir(new_file):
            os.mkdir(new_destination)
            static_to_public(new_file, new_destination)
        else:
            shutil.copy(new_file, destination)
    return
        



def extract_title(markdown):
    blocks = markdown.split("\n\n")
    for block in blocks:
        if block.startswith("#"):
            return block[1:].strip()



def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    markdown = open(from_path).read()
    template = open(template_path).read()
    html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    updated_template = template.replace("{{ Title }}", title).replace("{{ Content }}", html)
    dirs = dest_path.rsplit("/")
    if not os.path.lexists(dirs[0]):
        os.makedirs(dirs[0])
    with open(dest_path, 'w') as file:
        file.write(updated_template)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    file_list = os.listdir(dir_path_content)
    for file in file_list:
        new_destination = os.path.join(dest_dir_path, file)
        new_file = os.path.join(dir_path_content, file)
        if os.path.isdir(new_file):
            os.mkdir(new_destination)
            generate_pages_recursive(new_file, template, new_destination)
        else:
            new_destination = new_destination.split(".")
            new_destination = new_destination[0] +".html"
            generate_page(new_file, template, new_destination)
    return
        
