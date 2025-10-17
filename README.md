# Number Plate Recognition System

This is a small Flask-based number plate recognition project. It allows uploading a vehicle image, detects the number plate, and returns the cropped plate image along with the recognized text.

Below is an example using the sample image `google_images/133.jpeg` and the corresponding detected result `static/results/133_plate.jpg`.


![Original ](https://github.com/user-attachments/assets/289e4fe7-516e-48dc-b1bd-afa6189ffe6e)

![Detected plate](https://github.com/user-attachments/assets/d8564d26-7141-43b4-88be-0c39e9f96495)


How to run

1. Create a virtual environment and install dependencies (if any). This project is a simple Flask app — make sure Flask is installed.

   ```bash
   python -m venv venv
   source venv/Scripts/activate    # on Windows (PowerShell: venv\Scripts\Activate.ps1)
   pip install -r requirements.txt  # if you have one, otherwise: pip install flask
   ```

2. Start the app:

   ```bash
   python app.py
   ```

3. Open the site (usually http://127.0.0.1:5000/) to upload images and see recognition results.

Notes

- The README references the sample files by relative paths. If you move files, update the paths accordingly.
- If you want the README images to show on GitHub, ensure the `google_images/133.jpeg` and `static/results/133_plate.jpg` files are committed to the repository.

Tesseract OCR

- This project uses Tesseract OCR (the Python package `pytesseract` is a wrapper).
- On Windows, you can download a prebuilt Tesseract installer from the UB Mannheim builds:

  https://github.com/UB-Mannheim/tesseract/wiki

  After installing, ensure `tesseract.exe` is available and update the path in `detect.py` if necessary.
