from markdown_blocks import *
from markdown_convert import *
from htmlnode import *
from textnode import *
import re

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_block_list = []
    for block in blocks:
        match block_to_block_type(block):
            case "heading":
                count = heading_count(block)
                html_block_list.append(ParentNode(f"h{count}", block_to_textnode_to_html(block[count+1:])))
            case "code":
                html_block_list.append(ParentNode("code", block_to_textnode_to_html(block[3:-3])))
            case "quote":
                block = block.replace("\n> ", "")
                html_block_list.append(ParentNode("blockquote", block_to_textnode_to_html(block[2:])))
            case "unordered_list":
                block = list_tags(block, "unordered")
                html_block_list.append(ParentNode("ul", block))
            case "ordered_list":
                block = list_tags(block, "ordered")
                html_block_list.append(ParentNode("ol", block))
            case "paragraph":
                html_block_list.append(ParentNode("p", block_to_textnode_to_html(block)))
            case _:
                raise Exception("Unknown block type.")
    return ParentNode("div", html_block_list)




def heading_count(block):
    matches = re.findall(r"#+ ", block)
    return len(matches[0])-1


def block_to_textnode_to_html(block):
    nodes = text_to_textnodes(block)
    children_list = []
    for node in nodes:
        children_list.append(text_node_to_html_node(node))
    return children_list


def list_tags(block, list_type):
    lines = block.split("\n")
    html_lines = []
    for line in lines:
        if list_type == "ordered":
            line_sections = line.split(". ", 1)
            line = line_sections[1]
        if list_type =="unordered":
            line = line[2:]
        html_lines.append(ParentNode("li", block_to_textnode_to_html(line)))
    return html_lines



