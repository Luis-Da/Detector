# Importamos las librerias
import cv2
import numpy as np
import matplotlib.pyplot as plt


# Imagen
# Vamos a crear nuestra matriz principal
img = 100 * np.ones((10,10,3), np.uint8) # matriz de ceros de 10 *10 con 3 canales 

# Extraemos los canales
R = img[:,:,0] #matriz 0
G = img[:,:,1] #matriz 1
B = img[:,:,2] #matriz2

# Modificamos un canal (Rojo)
#R[:,:] = 0 #todoslospixeles de R en 0

# Modificamos l imagen
#img[:,:,0] = R

# Modificamos un canal (VERDE)
R[:,:] = 255
G[:,:] = 255
B[:,:] = 0

# Modificamos l imagen
# img[:,:,0] = R
# img[:,:,1] = G
# img[:,:,2] = B

# print(img)


# Mostramos nuestra imagen
plt.imshow(img)
plt.show()

# Con el teclado pasamos la imagen
cv2.waitKey(0)