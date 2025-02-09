import shutil

from termcolor import colored


def transfer_files(target_dir, source_dir):
    try:
        # Copy templates
        print(colored("INFO Copying HTML/MD templates...", "light_blue"))
        shutil.copytree(
            f"{source_dir}/.neuron-generator/templates", target_dir, dirs_exist_ok=True
        )

        shutil.copy2(
            f"{source_dir}/.neuron-generator/neuron.dhall",
            f"{target_dir}",
        )

        print(colored("SUCCESS Templates transferred", "light_green"))

        # Copy images to /static
        print(colored("INFO Copying static files...", "light_blue"))
        shutil.copytree(f"{source_dir}/img", f"{target_dir}/static", dirs_exist_ok=True)

        # Copy favicon
        shutil.copy2(
            f"{source_dir}/.neuron-generator/templates/favicon/favicon.ico",
            f"{target_dir}/static",
        )

        print(colored("SUCCESS Static files transferred", "light_green"))

        print(colored("INFO Copying zettels...", "light_blue"))

        # Copy notes
        shutil.copytree(f"{source_dir}/zk", f"{target_dir}", dirs_exist_ok=True)
        print(colored("SUCCESS Zettels transferred", "light_green"))
    except Exception as e:
        print(
            colored(
                f"ERROR Error occurred when transferring files: {str(e)}", "light_red"
            )
        )
