import os
import shutil
import uuid
from termcolor import colored
from constants import SOURCE, TARGET
from pathlib import Path


def create_source_dir():
    unique_dir_name = uuid.uuid4()
    if os.path.isdir(TARGET):
        shutil.rmtree(TARGET)

    # Create route directory and /static directory
    os.makedirs(f"{TARGET}/{str(unique_dir_name)}/static")
    print(
        colored(
            f"Created new Neuron output directory: {SOURCE}/{unique_dir_name}", "green"
        )
    )
    return unique_dir_name
