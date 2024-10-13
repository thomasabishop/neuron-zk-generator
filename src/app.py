from constants import SOURCE
from constants import TARGET
from lib.create_source_dir import create_source_dir


def main():
    output_dir = create_source_dir()
    print(output_dir)


if __name__ == "__main__":
    main()
