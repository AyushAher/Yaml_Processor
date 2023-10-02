import re
import yaml
import subprocess


class YamlRunner:
    def __init__(self, template):
        self.template = template
        self.data = yaml.safe_load(template)
        # Parse the template variable using the provided data
        parsed_result = self.parse_template_variable()
        parsed_result_yaml = yaml.safe_load(parsed_result)

        steps_lst = parsed_result_yaml['steps']

        for step in steps_lst:
            [*step_cmd] = step.split(' ')
            self.run_subprocess(step_cmd)

    @staticmethod
    def run_subprocess(step):
        try:
            # Run the command 'sudo stop service .net'
            result = subprocess.run(step, capture_output=True, text=True, check=True)

            # Print the standard output
            print("Standard Output:")
            print(result.stdout)

            # Print the return code (0 indicates success)
            print("Return Code:", result.returncode)

        except subprocess.CalledProcessError as e:
            # If the command returns a non-zero exit code, it's considered an error
            print("Error:", e)

    # Function to parse the template variable
    def parse_template_variable(self):
        # Define a regular expression pattern to match the template variable
        pattern = r'{{(.*?)}}'

        def replace_variable(match):
            # Extract the variable name from the matched pattern
            variable_name = match.group(1).strip()
            path_lst = variable_name.split('.')

            value = self.data
            try:
                for path_index in path_lst:
                    try:
                        path_index = int(path_index.replace('$', ''))
                    except:
                        pass
                    value = value[path_index]
            except:
                value = ''
            return value

        # Use re.sub to replace the template variable with its value
        parsed_template = re.sub(pattern, replace_variable, self.template)

        return parsed_template
