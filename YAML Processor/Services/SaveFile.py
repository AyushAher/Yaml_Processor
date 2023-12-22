from flask import request, jsonify
from Services.ProcessYaml import ProcessYAML


class FileUploader:
    def __init__(self, app):
        self.app = app
        self.allowed_extensions = {'yaml'}

        # Register the /upload endpoint
        self.app.add_url_rule('/upload', 'upload_file', self.upload_file, methods=['POST'])

    def allowed_file(self, filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in self.allowed_extensions

    def upload_file(self):
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'})

        file = request.files['file']

        if file.filename == '':
            return jsonify({'error': 'No selected file'})

        if file and self.allowed_file(file.filename):
            # Read the contents of the file without saving it
            file_contents = file.read()

            # Process the file_contents as needed
            # For example, you can parse YAML content here
            # Assuming you have a function 'process_yaml' to handle the content
            result = ProcessYAML(file_contents)

            return jsonify({'message': 'File processed successfully', 'result': result})

        return jsonify({'error': 'Invalid file format'})
