import sys
from Services.ProcessYaml import ProcessYAML


def main():

    if len(sys.argv) != 2:
        print("Usage: yaml_processor <yaml_file>")
        sys.exit(1)

    yaml_file = sys.argv[1]

    try:
        with open(yaml_file, "r") as f:
            yaml_data = f.read()

        ProcessYAML(yaml_data)

    except Exception as e:
        print("Error:", e)
        sys.exit(1)


if __name__ == "__main__":
    main()