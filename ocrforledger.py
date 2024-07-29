from tkinter import filedialog, Tk
import pytesseract as tess
from PIL import Image
import os
   
def preprocess_image(image_path):
    """Preprocess the image for better OCR results."""
    try:
        img = Image.open(image_path)
        # Additional preprocessing can be added here if needed
        return img
    except Exception as e:
        print(f"Error loading image {image_path}: {e}")
        return None

def extract_text_from_images(files):
    """Extract text from selected images."""
    texts = []
    for file in files:
        img = preprocess_image(file)
        if img:
            text = tess.image_to_string(img, lang='eng')
            texts.append(text)
        else:
            texts.append("Error processing image.")
    return texts

def extract():
    """Main function to extract text from images using a file dialog."""
    # Hide the root Tkinter window
    root = Tk()
    root.withdraw()

    # Open a file dialog to select multiple image files
    files = filedialog.askopenfilenames(title="Select Images", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.tiff")])
    
    if not files:
        print("No files selected.")
        return

    # Extract text from images
    texts = extract_text_from_images(files)

    # Print the extracted text
    for i, text in enumerate(texts):
        print(f"Text from file {os.path.basename(files[i])}:")
        print(text)
        print("-" * 40)

if __name__ == "__main__":
    extract()

