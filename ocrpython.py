import pytesseract
import os
from PIL import Image



def convert():
    img = Image.open("gg.jpeg")
    text = pytesseract.image_to_string(img)
    print(text)
convert()    