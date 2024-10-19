import os
import re
from termcolor import colored

image_rgx = r"!\[.*?\]\((.*?)\)"


def process_image_links(line, links):
    try:
        for link in links:
            stripped_img_ref = re.search(r"[^/\\]+$", link)
            if stripped_img_ref:
                stripped_img_ref = stripped_img_ref.group()
                new_img_ref = f"/static/{stripped_img_ref}"
                line = line.replace(f"({link})", f"({new_img_ref})")
        #        print(colored(f"     {links}", "green"))
        return line
    except Exception as e:
        print(colored(f" Error when transforming link: {str(e)}", "red"))


def transform_links(target_dir):
    print(colored("  Updating links...", "blue"))
    for filename in os.listdir(target_dir):
        if filename.endswith(".md"):
            file_path = os.path.join(target_dir, filename)
            with open(file_path, "r") as f:
                lines = f.readlines()

            modified = False
            new_lines = []
            for line in lines:
                img_links = re.findall(image_rgx, line)
                if img_links:

                    new_line = process_image_links(line, img_links)
                    new_lines.append(new_line)
                    modified = True
                else:
                    new_lines.append(line)

            if modified:
                with open(file_path, "w") as f:
                    f.writelines(new_lines)
    print(
        colored(
            "  Links updated!",
            "green",
        )
    )
