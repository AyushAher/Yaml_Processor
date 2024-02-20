from Services.Yaml_Runner import YamlRunner
import sys


class ProcessYAML:
    def __init__(self, yaml_data):
        # os_platform = sys.platform
        # if not os_platform.startswith('linux'):
        #     raise Exception(f"{os_platform} OS Not supported yet!")
       YamlRunner(yaml_data)
