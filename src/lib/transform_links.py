import os
import re

from termcolor import colored


def process_line(line):
        image_rgx = r"!\[.*?\]\((.*?)\)"
        internal_link_rgx = r"\[.*?\]\((.*?)\)"
        img_links = re.findall(image_rgx, line)
        internal_links = re.findall(internal_link_rgx, line) 
        
        if img_links:
            for img_link in img_links:
                stripped_img_ref = re.search(r"[^/\\]+$", img_link)
                if stripped_img_ref:
                    stripped_img_ref = stripped_img_ref.group()
                    new_img_ref = f"static/{stripped_img_ref}"
                    line = line.replace(f"({img_link})", f"({new_img_ref})")
        
        if internal_links:
            for internal_link in internal_links:
                if internal_link.endswith('.md') and ('/' in internal_link):
                    stripped_path = (re.search(r"[^/\\]+$", internal_link))
                    if stripped_path:
                        stripped_path = stripped_path.group()
                        line = line.replace(f"({internal_link})", f"({stripped_path})")   
        return line


def transform_links(target_dir):
    print(colored("INFO: Updating links...", "light_blue"))
    for filename in os.listdir(target_dir):
        if filename.endswith(".md"):
            file_path = os.path.join(target_dir, filename)
            with open(file_path, "r") as f:
                lines = f.readlines()

            new_lines = []
            for line in lines:
                new_lines.append(process_line(line))
            if len(new_lines): 
                with open(file_path, "w") as f:
                    f.writelines(new_lines)
    print(
        colored(
            "SUCCESS Links updated",
            "light_green",
        )
    )
