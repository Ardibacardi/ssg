import os
from markdown_block import markdown_to_html_node

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    title = extract_title(markdown_content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)


def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    else:
        raise Exception("No title found")
    
def generate_pages_recursive(content_path, template_path, dest_path):
    print(f"Scanning directory: {content_path}")
    for file in os.listdir(content_path):
        # Skip the public directory
        if file == "public":
            continue
            
        full_path = os.path.join(content_path, file)
        # Calculate relative path from content directory
        relative_path = os.path.relpath(full_path, content_path)
        dest_file_path = os.path.join(dest_path, relative_path)
        
        if os.path.isdir(full_path):
            # Create the directory if it doesn't exist
            os.makedirs(dest_file_path, exist_ok=True)
            generate_pages_recursive(full_path, template_path, dest_file_path)
        elif file.endswith('.md'):
            dest_html_path = dest_file_path.replace('.md', '.html')
            generate_page(full_path, template_path, dest_html_path)
    