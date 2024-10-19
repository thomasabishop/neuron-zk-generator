import shutil
from termcolor import colored


def transfer_files(target_dir, source_dir):
    try:
        # Copy templates
        print(colored("  Copying HTML/MD templates...", "blue"))
        shutil.copytree(
            f"{source_dir}/.neuron-generator/templates", target_dir, dirs_exist_ok=True
        )
        neuron_template = open(f"{target_dir}/neuron.dhall", "x")
        neuron_template.close()
        print(colored("  Templates transferred!", "green"))

        # Copy images to /static
        print(colored("  Copying static files...", "blue"))
        shutil.copytree(
            f"{source_dir}/img",
            f"{target_dir}/static",
        )
        print(colored("  Static files transferred!", "green"))

        print(colored("  Copying zettels...", "blue"))

        # Copy notes
        shutil.copytree(f"{source_dir}/zk", f"{target_dir}", dirs_exist_ok=True)
        print(colored("  Zettels transferred!", "green"))
    except Exception as e:
        print(colored(f"  Error occurred when transferring files: {str(e)}", "red"))
