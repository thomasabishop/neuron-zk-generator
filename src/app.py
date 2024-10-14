from constants import SOURCE
from constants import TARGET
from lib.create_target_dir import create_target_dir
from lib.transfer_files import transfer_files


def main():
    target_dir = create_target_dir(TARGET, SOURCE)
    transfer_files(f"{TARGET}/{target_dir}", SOURCE)


if __name__ == "__main__":
    main()
