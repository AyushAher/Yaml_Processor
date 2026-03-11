import re
import yaml
import shlex
import subprocess


class YamlRunner:

    def __init__(self, template: str):
        try:
            # Load YAML safely
            self.template = template
            self.data = yaml.safe_load(template)

            if not isinstance(self.data, dict):
                raise ValueError("Invalid YAML format")

            # Resolve template variables
            parsed_template = self.parse_template_variable()

            # Parse again after template resolution
            parsed_yaml = yaml.safe_load(parsed_template)

            if "steps" not in parsed_yaml:
                raise ValueError("YAML must contain a 'steps' section")

            steps = parsed_yaml["steps"]

            if not isinstance(steps, list):
                raise ValueError("'steps' must be a list")

            for step in steps:
                self.execute_step(step)

        except Exception as e:
            raise RuntimeError(f"YAML processing failed: {str(e)}")

    def execute_step(self, step: str):
        if not isinstance(step, str):
            raise ValueError(f"Invalid step format: {step}")

        print(f"\nExecuting step: {step}")

        # Safe command parsing
        cmd = shlex.split(step)

        try:
            result = subprocess.run(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=False,
                text=True,
                check=True
            )

            if result.stdout:
                print("Output:")
                print(result.stdout)

        except subprocess.CalledProcessError as e:
            print("Error occurred:")
            print(e.stderr)
            raise

    def parse_template_variable(self):
        pattern = r'{{(.*?)}}'

        def replace_variable(match):
            variable_name = match.group(1).strip()
            path_lst = variable_name.split('.')

            value = self.data

            try:
                for path_index in path_lst:
                    # Handle list index syntax like $0
                    if path_index.startswith("$"):
                        index = int(path_index[1:])
                        value = value[index]
                    else:
                        value = value[path_index]

                return str(value)

            except Exception:
                raise ValueError(f"Invalid template variable: {variable_name}")

        parsed_template = re.sub(pattern, replace_variable, self.template)

        return parsed_template