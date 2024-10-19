import os
from pathlib import Path


def list_entries(source_dir):
    entries = []
    with os.scandir(source_dir) as dir_contents:
        for entry in dir_contents:
            if Path(entry).suffix == ".md":
                file_name = Path(entry).stem
                info = entry.stat()
                entries.append({"file_name": file_name, "modified": info.st_mtime})
    return entries
