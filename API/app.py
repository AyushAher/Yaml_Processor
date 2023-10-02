from flask import Flask
from Services.SaveFile import FileUploader
from Services.ProcessYaml import *

app = Flask(__name__)

# Initialize the FileUploader class from savefile.py
uploader = FileUploader(app)


# Define additional routes and functionality for your Flask app
@app.route('/')
def home():
    return 'Hellloo'


@app.route('/process')
def process_yaml():
    with open('sample.yaml', 'r') as file:
        # Read the entire content of the file into a string
        file_contents = file.read()
        process_data = ProcessYAML(file_contents)
        file.close()

    return process_data.process_yaml()


if __name__ == '__main__':
    app.run(debug=True)
