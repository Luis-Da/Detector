import cv2
import numpy as np
import pytesseract
from PIL import Image
from datetime import datetime
import mysql.connector

# Configuración de la conexión a la base de datos
config = {
    'user': 'root',
    'password': 'example',
    'host': 'localhost',  # Utiliza localhost si ejecutas la aplicación Python en la misma máquina que Docker
    'port': 3306,
    'database': 'mydatabase',
}

# Función para tomar una foto y guardarla en disco
def tomar_foto(frame, output_folder):
    # Obtener la fecha y hora actual
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d_%H%M%S")
    output_path = f"{output_folder}/foto_capturada_{timestamp}.png"

    cv2.imwrite(output_path, frame)
    print("Foto de placa capturada:", output_path)

# Función para validar y filtrar las placas detectadas
def validar_elementos_lista(lista):
    elementos_validos = []
    for texto in lista:
        if len(texto) == 7 and texto.isalpha() and texto[:3].isupper() and texto[3] in " -" and texto[4:7].isdigit():
            elementos_validos.append(texto)
    return elementos_validos

# Función para eliminar saltos de línea en el texto
def eliminar_salto_de_linea(lista):
    nueva_lista = [elem.replace('\n', '') for elem in lista]
    return nueva_lista

# Crear una conexión a la base de datos
connection = mysql.connector.connect(**config)

# Crear un cursor para ejecutar comandos SQL
cursor = connection.cursor()

# Código SQL para insertar un registro en la tabla "vehiculos"
sql_insert = "INSERT INTO vehiculos (placa, ubicacion, fecha, registro) VALUES (%s, %s, %s, %s)"

# Ruta del archivo de configuración de Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\luis.acevedo\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# Parámetros de Tesseract OCR
config_tesseract = "--oem 1 --psm 6"

# Ruta para almacenar las fotos
output_folder = "registro_fotografico"

# Captura de video
video_path = "4placas.mp4"
cap = cv2.VideoCapture(video_path)

# Listas para almacenar las placas detectadas
lista = []
resultados_placas = []

# Bucle principal para capturar y procesar los fotogramas del video
while True:
    ret, frame = cap.read()

    if not ret:
        break

    # ... (código para la detección de placas y procesamiento de los fotogramas omitido para brevedad)

    # Extraer la imagen binarizada y convertirla en un arreglo de NumPy
    bin_array = np.array(bin)
    bin_array = bin_array.reshape(alp, anp)
    bin_array = Image.fromarray(bin_array)
    bin_array = bin_array.convert("L")
    bin_array = np.array(bin_array)
    bin_array = cv2.imencode('.png', bin_array)[1].tobytes()

    # Validar si hay una placa detectada y guardarla en la base de datos
    if resultados_placas:
        valor_mas_repetido = max(resultados_placas, key=lambda x: resultados_placas.count(x))
        repeticiones = resultados_placas.count(valor_mas_repetido)
        print("Posible Placa", valor_mas_repetido)

        ubicacion = "antioquia"  # Puedes ajustar esto según el lugar donde se realiza la detección
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        datos_vehiculo = (valor_mas_repetido, ubicacion, fecha, bin_array)
        cursor.execute(sql_insert, datos_vehiculo)
        connection.commit()

        resultados_placas.clear()  # Limpiar la lista de resultados después de guardar los datos

    # Mostrar la imagen con los contornos y la posible placa
    cv2.imshow('vehiculos', frame)

    # Leer una tecla para salir (presionar "Esc" para salir)
    t = cv2.waitKey(1)
    if t == 27:
        break

# Cerrar el cursor y la conexión a la base de datos
cursor.close()
connection.close()

# Liberar los recursos y cerrar todas las ventanas
cap.release()
cv2.destroyAllWindows()
