from textnode import *
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    node_list = []
    for old_node in old_nodes:
        if old_node.text_type != "text":
             node_list.append(old_node)
        else:
            node_parts = []
            parts = old_node.text.split(delimiter)
            if len(parts) % 2 == 0:
                raise ValueError("Even amount of parts; missing delimiter")
            for i in range(len(parts)):
                if parts[i] == "":
                    continue
                if i % 2 == 0:
                    node_parts.append(TextNode(parts[i], "text"))
                else:
                    node_parts.append(TextNode(parts[i], text_type))
            node_list.extend(node_parts)
    return node_list
       
def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)

def split_nodes_link(old_nodes):
    node_list = []
    for old_node in old_nodes:
        if old_node.text_type != "text":
             node_list.append(old_node)
             continue
        links = extract_markdown_links(old_node.text)
        old_node_text = old_node.text
        if len(links) == 0:
            node_list.append(old_node)
            continue
        for i, link in enumerate(links):
            node_parts = []
            parts = old_node_text.split(f"[{link[0]}]({link[1]})", 1)
            if parts[0] != "":
                node_parts.append(TextNode(parts[0], "text"))
            node_parts.append(TextNode(link[0], "link", link[1]))
            old_node_text = "".join(parts[1:])
            if i == len(links) - 1 and parts[1] != "":
                node_parts.append(TextNode(parts[1], "text"))
            node_list.extend(node_parts)
    return node_list

def split_nodes_image(old_nodes):
    node_list = []
    for old_node in old_nodes:
        if old_node.text_type != "text":
             node_list.append(old_node)
             continue
        images = extract_markdown_images(old_node.text)
        old_node_text = old_node.text
        if len(images) == 0:
            node_list.append(old_node)
            continue
        for i, image in enumerate(images):
            node_parts = []
            parts = old_node_text.split(f"![{image[0]}]({image[1]})", 4)
            if parts[0] != "":
                node_parts.append(TextNode(parts[0], "text"))
            node_parts.append(TextNode(image[0], "image", image[1]))
            old_node_text = "".join(parts[1:])
            if i == len(images) - 1 and parts[1] != "":
                node_parts.append(TextNode(parts[1], "text"))
            node_list.extend(node_parts)
    return node_list


def text_to_textnodes(text):
    node = TextNode(text, "text",)
    new_nodes = split_nodes_delimiter([node], "**", "bold")
    new_nodes = split_nodes_delimiter(new_nodes, "*", "italic")
    new_nodes = split_nodes_delimiter(new_nodes, "`", "code")
    new_nodes = split_nodes_image(new_nodes)
    new_nodes = split_nodes_link(new_nodes)
    return new_nodes


