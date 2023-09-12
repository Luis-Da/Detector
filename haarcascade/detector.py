import cv2

# Cargar el archivo XML del Haar cascade preentrenado
car_cascade = cv2.CascadeClassifier('cars2.xml')
motorbike_cascade = cv2.CascadeClassifier('two_wheeler.xml')

# Función para detectar objetos en una imagen
def detect_objects(cascade, image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)):
    # Convertir la imagen a escala de grises
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Detectar objetos utilizando el Haar cascade
    objects = cascade.detectMultiScale(gray, scaleFactor=scaleFactor, minNeighbors=minNeighbors, minSize=minSize)
    
    # Dibujar los rectángulos alrededor de los objetos detectados
    for (x, y, w, h) in objects:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    return image

# Cargar la imagen de entrada
image = cv2.imread('carros.jpg')

# Detectar carros y motos en la imagen
image_with_cars = detect_objects(car_cascade, image)
image_with_motorbikes = detect_objects(motorbike_cascade, image)

# Mostrar las imágenes con los objetos detectados
cv2.imshow('Cars', image_with_cars)
cv2.imshow('Motorbikes', image_with_motorbikes)
cv2.waitKey(0)
cv2.destroyAllWindows()
