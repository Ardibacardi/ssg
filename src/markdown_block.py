import re
from htmlnode import ParentNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"


def markdown_to_blocks(markdown):
    blocks = markdown.split('\n\n')
    filtered_blocks = [block.strip() for block in blocks if block != ""]
    return filtered_blocks

def block_to_block_type(block) -> str:
    lines = block.split('\n')
    if bool(re.match(r'^#{1,6}\s', block)):
        return block_type_heading
    if len(lines) > 1 and lines[0].startswith('```') and lines[-1].startswith('```'):
        return block_type_code
    if block.startswith('>'):
        return block_type_quote
    if block.startswith('* ') or block.startswith('- '):
        return block_type_ulist
    if bool(re.match(r'^\d+\.\s', block)):
        return block_type_olist
    return block_type_paragraph

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children, None)

def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == block_type_heading:
        return block_to_header(block)
    elif block_type == block_type_code:
        return block_to_code(block)
    elif block_type == block_type_quote:
        return block_to_quote(block)
    elif block_type == block_type_ulist:
        return block_to_ulist(block)
    elif block_type == block_type_olist:
        return block_to_olist(block)
    else:
        return block_to_paragraph(block)
    
def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children

def block_to_header(block):
    count = 0
    for char in block:
        if char == '#':
            count += 1
        else:
            break
    text = block[count + 1:]
    children = text_to_children(text)
    return ParentNode(f'h{count}', children)

def block_to_paragraph(block):
    children = text_to_children(" ".join(block.split('\n')))
    return ParentNode("p", children)

def block_to_code(block):
    text = block[4:-3]
    children = text_to_children(text)
    code = ParentNode("code", children)
    return ParentNode("pre", [code])

def block_to_quote(block):
    lines = block.split('\n')
    new_lines = []
    for line in lines:
        new_lines.append(line.lstrip('> ').strip())
    children = text_to_children(" ".join(new_lines))
    return ParentNode("blockquote", children)

def block_to_ulist(block):
    items = block.split('\n')
    html_items = []
    for item in items:
        children = text_to_children(item[2:])
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)

def block_to_olist(block):
    items = block.split('\n')
    html_items = []
    for item in items:
        children = text_to_children(item[3:])
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)

