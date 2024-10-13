import os
import shutil
from constants import SOURCE, TARGET
from pathlib import Path


def copy_zettels():
    if os.path.isdir(TARGET):
        shutil.rmtree(TARGET)

    # p.mkdir()
