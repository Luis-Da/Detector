import pytesseract
from PIL import Image
import os

# Prefijo para el nombre de las imágenes de salida
#output_prefix = 'output/image'

#Ruta al archivo de palabras personalizado
diccionario = ''

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\luis.acevedo\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'



def convert_image_to_text(image_path):
    custom_config = r'--oem 1 --psm 6 -l spa --user-words {}'.format(diccionario)
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image, config=custom_config)
    return text


output_folder = 'placas/'
image_files = sorted(os.listdir(output_folder))
final_text = ""
print(final_text)
