import cv2 
from PIL import Image
import pytesseract
import os
from tkinter import Tk, filedialog

# If Tesseract is not in your PATH, specify the path to the executable
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def preprocess_image(image_path):
    # Read image with OpenCV
    img = cv2.imread(image_path)

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply some preprocessing (e.g., thresholding)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

    # Save the processed image temporarily
    temp_image_path = 'temp.png'
    cv2.imwrite(temp_image_path, thresh)
    
    return temp_image_path

def extract_text(image_path, lang='eng'):
    # Preprocess the image
    processed_image_path = preprocess_image(image_path)

    # Load the processed image with PIL
    processed_image = Image.open(processed_image_path)

    # Perform OCR
    text = pytesseract.image_to_string(processed_image, lang=lang)

    return text

if __name__ == '__main__':
    # Create a Tkinter root window (it will not be shown)
    root = Tk()
    root.withdraw()  # Hide the root window

    # Open a file dialog to select multiple image files
    image_paths = filedialog.askopenfilenames(
        title="Select Image Files",
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.tiff")]
    )

    if image_paths:
        for image_path in image_paths:
            if os.path.exists(image_path):
                # Extract text from image
                text = extract_text(image_path)
                
                # Print the extracted text
                print(f"Text from {image_path}:")
                print(text)
                print("-" * 40)
            else:
                print(f"File {image_path} does not exist.")
    else:
        print("No files selected.")
