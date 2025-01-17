import json
import subprocess

from termcolor import colored


def invoke_eolas_db():
    process = subprocess.run(
        ["eolas-db", "export-tags"],
        capture_output=True,
        text=True,
    )
    return json.loads(process.stdout)


def generate_tag_file(target_dir):
    try:
        print(colored("INFO Creating tag file...", "light_blue"))
        tag_file = f"{target_dir}/tags.md"
        tag_index = invoke_eolas_db()
        print(tag_index["time"])
        with open(tag_file, "a") as file:
            for tag in tag_index:
                file.write(f"[{tag}](./tags#{tag}), ")
            file.write("\n\n")
            for tag in tag_index:
                file.write(f"### {tag} \n\n")
                for entry in tag_index[tag]:
                    file.write(f"- [[{entry}]] \n")
    except Exception as e:
        print(
            colored(
                f"ERROR Error occurred when creating tag file: {str(e)}", "light_red"
            )
        )

    # check with open syntax
