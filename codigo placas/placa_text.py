import pytesseract
from PIL import Image
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\luis.acevedo\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

def convert_image_to_text(image_path, dpi):
    custom_config = r'--oem 3 --psm 7 -l spa --dpi {} --user-words {}'.format(dpi, diccionario)
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image, config=custom_config)
    return text

diccionario = ''  # Ruta al archivo de palabras personalizado
output_folder = 'placas/'
image_files = sorted(os.listdir(output_folder))
final_text = ""
dpi = 10  # Valor deseado para el parámetro DPI

for image_file in image_files:
    image_path = os.path.join(output_folder, image_file)
    text = convert_image_to_text(image_path, dpi)
    final_text += text

print(final_text)
