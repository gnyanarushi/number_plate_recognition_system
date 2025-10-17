from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename
from detect import recognize_plate

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join('static', 'uploads')
app.config['RESULT_FOLDER'] = os.path.join('static', 'results')

# Ensure upload/result folders exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['RESULT_FOLDER'], exist_ok=True)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "No file uploaded"

    file = request.files['file']
    if file.filename == '':
        return "No selected file"

    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    # Call detect to process and save a result image inside RESULT_FOLDER
    text, plate_filename = recognize_plate(filepath, app.config['RESULT_FOLDER'])

    return render_template('result.html', text=text, plate_image=plate_filename, uploaded_filename=filename)


if __name__ == '__main__':
    app.run(debug=True)
