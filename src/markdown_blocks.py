import re


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    stripped_blocks = []
    for block in blocks:
        if block == "":
            continue
        stripped_blocks.append(block.strip())
    return stripped_blocks




def block_to_block_type(block):
    if re.match(r"#+ ", block):
        return "heading"
    if re.match(r"```", block):
        if re.search(r"```$", block):
            return "code"
    newline_count = len(re.findall("\n", block))
    if len(re.findall("\n[>]", block)) == newline_count and block.startswith(">"):
        return "quote"
    if len(re.findall("\n[*-] ", block)) == newline_count and re.match(r"[*-] ", block):
        return "unordered_list"
    ordered_list_check = re.findall("\n[\d]+\. ", block)
    if len(ordered_list_check) == newline_count and re.match(r"1\. ", block):
        for item in range(len(ordered_list_check)):
            if item + 2 != int(ordered_list_check[item][1:-2]):
                return "paragraph"
        return "ordered_list"
    return "paragraph"
