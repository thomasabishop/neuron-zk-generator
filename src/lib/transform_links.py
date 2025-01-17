import os
import re

from termcolor import colored


def process_line(line):
    link_rgx = r"\[.*?\]\((.*?)\)"
    links = re.findall(link_rgx, line)

    if links:
        for link in links:
            stripped_path = re.search(r"[^/\\]+$", link)
            if stripped_path:
                stripped_path = stripped_path.group()
                # Handle internal links
                if ".md" in stripped_path:
                    line = line.replace(f"({link})", f"({stripped_path})")
                    # Handle image links
                else:
                    new_img_path = f"static/{stripped_path}"
                    line = line.replace(f"({link})", f"({new_img_path})")
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
