import os
import shutil
import uuid
from termcolor import colored


def create_target_dir(target_dir, source_dir):
    try:
        unique_dir_name = uuid.uuid4()

        # Overwrite existing output directory
        if os.path.isdir(target_dir):
            shutil.rmtree(target_dir)

        # Create new output directory
        os.makedirs(f"{target_dir}/{str(unique_dir_name)}")
        print(
            colored(
                f"  Created new Neuron output directory: {source_dir}/{unique_dir_name}",
                "green",
            )
        )
        return unique_dir_name

    except Exception as e:
        print(
            colored(
                f"  Error occurred when creating target directory: {str(e)}", "red"
            )
        )
