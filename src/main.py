import os
import shutil

from copystatic import copy_static_files
from generate import generate_pages_recursive

static_path = "./static"
public_path = "./public"
content_path = "./content"
template_path = "./template.html"

def main():
    print("DELETING OLD PUBLIC FOLDER")
    if os.path.exists(public_path):
        shutil.rmtree(public_path)

    print("COPYING STATIC FILES")
    copy_static_files(static_path, public_path)

    print("GENERATING PAGES")
    generate_pages_recursive(
        content_path,
        template_path,
        public_path
    )


if __name__ == "__main__":
    main()