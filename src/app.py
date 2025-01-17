import subprocess

from lib.create_target_dir import create_target_dir
from lib.generate_index_file import generate_index_file
from lib.generate_tag_file import generate_tag_file
from lib.transfer_files import transfer_files
from lib.transform_links import transform_links

SOURCE = "/home/thomas/repos/eolas"
TARGET = "/home/thomas/repos/eolas/neuron"
SLACK_NOTIFIER = "/home/thomas/repos/slack-notifier/src/index.js"


def main():
    try:
        build_id = create_target_dir(TARGET, SOURCE)
        transfer_files(f"{TARGET}/{build_id}", SOURCE)
        transform_links(f"{TARGET}/{build_id}")
        generate_index_file(f"{TARGET}/{build_id}", build_id, SOURCE)
        generate_tag_file(f"{TARGET}/{build_id}")
        subprocess.run(
            [
                "node",
                SLACK_NOTIFIER,
                "eolas",
                f"✅ Neuron static site successfully generated locally for Eolas. Build: {build_id}",
            ]
        )
    except Exception as e:
        subprocess.run(
            [
                "node",
                SLACK_NOTIFIER,
                "eolas",
                f"⛔ Neuron static site generation failed for Eolas: {e}",
            ]
        )


if __name__ == "__main__":
    main()
