import cv2
import numpy as np # para trabajar la imagenes como matriz
import matplotlib.pyplot as plt # para pltear y manipular las imagenes

# Imagen Negra
# Vamos a crear nuestra imagen negra
img = np.zeros((10,10,1), np.uint8)# matriz de ceros de 10 *10 con color 1 

# Cambiamos algunos pixeles img[x,Y] x->filas y->columnas
img[0,1] = 30.8
img[2,3] = 50
img[4,5] = 200
img[6,7] = 140

# Mostramos los valores numericos
print(img)

plt.imshow(img,cmap="gray")
plt.show()

#las imagnes a blanco y negro tienen un solo canal; las imagenes a color tiene 3 canales entonces se componen por 3 matrices superpuestas RGB