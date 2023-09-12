import cv2
import pytesseract

# Configurar la ubicación del ejecutable de Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\luis.acevedo\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# Parámetros de acceso a la cámara
USERNAME = ''
PASSWORD = ''
IP = 'IP'
PORT = ''
# URL de la transmisión de la cámara
URL = "rtsp://{}:{}@{}:{}/onvif1".format(USERNAME, PASSWORD, IP, PORT)
print('Conectando a: ' + URL)
cap = cv2.VideoCapture(URL)

while True:
    ret, frame = cap.read()
    if ret == False:
        break

    # Dibujar un rectángulo
    cv2.rectangle(frame, (870, 750), (1070, 850), (0, 0, 0), cv2.FILLED)
    cv2.putText(frame, Ctexto[0:7], (900, 810), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Extraer el ancho y el alto de los fotogramas
    al, an, c = frame.shape

    # Tomar el centro de la imagen en X
    x1 = int(an / 3)
    x2 = int(x1 * 2)

    # En Y
    y1 = int(al / 3)
    y2 = int(y1 * 2)

    # Texto
    cv2.rectangle(frame, (x1 + 160, y1 + 500), (1120, 940), (0, 0, 0), cv2.FILLED)
    cv2.putText(frame, 'Procesando Placa', (x1 + 180, y1 + 550), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Ubicar el rectángulo en las zonas extraídas
    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # Recorte de la zona de interés
    recorte = frame[y1:y2, x1:x2]

    # Preprocesamiento de la zona de interés
    gray = cv2.cvtColor(recorte, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # Reconocimiento de caracteres con Tesseract OCR
    custom_config = r'--oem 1 --psm 7 -l spa'
    text = pytesseract.image_to_string(thresh, config=custom_config)

    # Dibujar el texto en el frame principal
    cv2.putText(frame, text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Mostrar el frame
    cv2.imshow('Reconocimiento de Placa', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar los recursos
cap.release()
cv2.destroyAllWindows()
