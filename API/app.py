from flask import Flask, render_template
from Services.SaveFile import FileUploader
from Services.ProcessYaml import *

app = Flask(__name__)

# Initialize the FileUploader class from savefile.py
uploader = FileUploader(app)

# Define additional routes and functionality for your Flask app
@app.route('/')
def home():
    return "Fuck You!"

if __name__ == '__main__':
    app.run()
