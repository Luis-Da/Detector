import cv2
import numpy as np
import pytesseract
from PIL import Image
from datetime import datetime

def tomar_foto(video_path, frame_num, output_folder):
    cap = cv2.VideoCapture(video_path)
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_num)
    ret, frame = cap.read()

    # Obtener la fecha y hora actual
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d_%H%M%S")
    output_path = f"{output_folder}/foto_capturada_{timestamp}.png"

    cv2.imwrite(output_path, frame)

    cap.release()
    cv2.destroyAllWindows()

def validar_elementos_lista(lista):
    elementos_validos = []
    for texto in lista:
        if len(texto) == 7 and texto[0:2].isalpha() and texto[3] in " -" and texto[4:].isdigit():
            elementos_validos.append(texto)
    return elementos_validos

def eliminar_salto_de_linea(lista):
    nueva_lista = [elem.replace('\n', '') for elem in lista]
    return nueva_lista

# Captura de video
video_path = "Vmt1.MOV"
cap = cv2.VideoCapture(video_path)
lista = []
frame_num = 1
output_folder = "registro_fotografico"
# Variable para rastrear si hay una matrícula en la ROI
plate_detected = False

# Ciclo para capturar los fotogramas en el video
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Definir la ROI
    x1, y1, x2, y2 = 870, 750, 1070, 850

    # Dibujar el rectángulo, los fotogramas quedan almacenados en frame
    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), cv2.FILLED)
    cv2.putText(frame, "", (900, 810), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Recorte de la ROI
    roi = frame[y1:y2, x1:x2]

    # Preprocesamiento de la zona de interés
    gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    _, bin_roi = cv2.threshold(gray_roi, 40, 255, cv2.THRESH_BINARY)

    # Convertir la matriz en una imagen
    bin_roi_pil = Image.fromarray(bin_roi)

    # Especificar un tamaño para la placa 
    if y2 - y1 >= 35 and x2 - x1 >= 85:
        if not plate_detected:
            tomar_foto(video_path, frame_num, output_folder)
            print("Se está tomando la foto")
            plate_detected = True

        # Ruta de tesseract
        pytesseract.pytesseract.tesseract_cmd = r'C:\Users\luis.acevedo\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
        # Parámetros de tesseract
        config = "--oem 1 --psm 6 "
        texto = pytesseract.image_to_string(bin_roi_pil, config=config)
        # Definir los caracteres a omitir
        caracteres_a_omitir = "!@#$%^&*()_+{}[]|\:;<>?,./?¡""''¥=¿~~~~????"
        texto = ''.join(c for c in texto if c not in caracteres_a_omitir)

        if len(texto) == 7 and texto[0].isalpha() and texto[1].isalpha() and texto[2].isalpha() \
                and texto[4].isdigit() and texto[5].isdigit():
            lista.append(texto)

    # Si plate_detected es True, la matrícula ha sido detectada en la ROI, pero aún no ha salido completamente
    if plate_detected and (y1 > 850 or y2 < 750 or x1 > 1070 or x2 < 870):
        # La matrícula ha salido completamente de la ROI
        print("La placa ha salido de la ROI:", texto)
        plate_detected = False  # Reiniciar para detectar una nueva matrícula

        # Imprimir la imagen y los resultados
        resul = eliminar_salto_de_linea(lista)
        opplacas = validar_elementos_lista(resul)

        valor_mas_repetido = max(opplacas, key=lambda x: opplacas.count(x))
        repeticiones = opplacas.count(valor_mas_repetido)

        print("Posible Placa:", valor_mas_repetido)
        print("Repeticiones:", repeticiones)

        lista = []  # Reiniciar la lista para el nuevo ciclo

    # Mostrar recorte gris
    cv2.imshow('vehiculos', frame)

    # Leer una tecla para salir
    t = cv2.waitKey(1)

    if t == 27:
        break

cap.release()
cv2.destroyAllWindows()

