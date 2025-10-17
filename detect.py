import cv2
import pytesseract
import numpy as np
import os

# Set tesseract path if needed
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def recognize_plate(image_path, result_folder=None):
    """Recognize plate from image_path and save result image into result_folder.

    Returns: (text, result_filename)
    """
    img = cv2.imread(image_path)
    if img is None:
        return "Could not read image", None

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply edge detection
    edges = cv2.Canny(gray, 100, 200)

    # Find contours
    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    plate = None

    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        aspect_ratio = w / float(h)
        if 2 < aspect_ratio < 6 and w > 100 and h > 30:
            plate = img[y:y + h, x:x + w]
            break

    if plate is not None:
        # Preprocess the plate image
        plate_gray = cv2.cvtColor(plate, cv2.COLOR_BGR2GRAY)
        plate_gray = cv2.bilateralFilter(plate_gray, 11, 17, 17)
        _, plate_thresh = cv2.threshold(plate_gray, 150, 255, cv2.THRESH_BINARY)

        # OCR
        text = pytesseract.image_to_string(plate_thresh, config='--psm 8')
        text = ''.join(filter(str.isalnum, text))

        # Save cropped plate for display inside result_folder
        if result_folder is None:
            result_folder = os.path.join('static', 'results')
        os.makedirs(result_folder, exist_ok=True)

        # Create a unique filename based on input image name
        base = os.path.splitext(os.path.basename(image_path))[0]
        result_filename = f"{base}_plate.jpg"
        result_path = os.path.join(result_folder, result_filename)
        cv2.imwrite(result_path, plate)
        return text, result_filename

    # No plate found: copy the original image to results for reference
    if result_folder is None:
        result_folder = os.path.join('static', 'results')
    os.makedirs(result_folder, exist_ok=True)
    base = os.path.splitext(os.path.basename(image_path))[0]
    result_filename = f"{base}_no_plate.jpg"
    result_path = os.path.join(result_folder, result_filename)
    cv2.imwrite(result_path, img)
    return "No plate detected", result_filename
