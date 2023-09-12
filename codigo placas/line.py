import cv2
import numpy as np
import pytesseract
from PIL import Image
from datetime import datetime


def tomar_foto(frame, output_folder):
    # Obtener la fecha y hora actual
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d_%H%M%S")
    output_path = f"{output_folder}/foto_capturada_{timestamp}.png"

    cv2.imwrite(output_path, frame)
    print("Foto de placa capturada:", output_path)


def validar_elementos_lista(lista):
    elementos_validos = []
    for texto in lista:
        if len(texto) == 7 and texto[0] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" and texto[1] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" and \
                texto[2] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" and (texto[3] == " " or texto[3]=="-") and all(
                c != " " for c in texto[0:3] + texto[4:7]) and all(j  in "1234567890" for j in texto[4:6]):
            elementos_validos.append(texto)
    return elementos_validos


def eliminar_salto_de_linea(lista):
    nueva_lista = [elem.replace('\n', '') for elem in lista]
    return nueva_lista





# captura de video
video_path= "Rapidos1.mov"
cap = cv2.VideoCapture( video_path)
lista = []
Ctexto = ""


output_folder = "registro fotografico"
# Definir la condición para capturar la foto (puedes ajustar esto según tus necesidades)
condicion = True#condicion foto
detectar=False

# captura de los fotogramas en el video
while True :
    ret, frame = cap.read()
    if not ret:
        break
    # dibujamos el rectangulo, los fotogramas quedan almacenado en frame
    cv2.rectangle(frame, (870, 750), (1070, 850), (0, 0, 0), cv2.FILLED)
    cv2.putText(frame, Ctexto[0:7], (900, 810), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)


    

    # EXTRAEMOS  el ancho , el alto de los fotogramas
    al, an, c = frame.shape

    # tomar centro de imagen
    x1 = int(an / 3)
    x2 = int(x1 * 2)

    y1 = int(al / 3)
    y2 = int(y1 * 2)

    # texto
    cv2.rectangle(frame, (x1 + 160, y1 + 500), (1120, 940), (0, 0, 0), cv2.FILLED)
    cv2.putText(frame, 'procesando placas', (x1 + 180, y1 + 550), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # ubicamos el rectangulo en la zona extraida
    cv2.rectangle(frame, (x1, y1 ), (x2, y2), (0, 255, 0), 2)
   # cv2.line(frame, (x1, y1+100), (x2, y1+100), (100, 0, 0), 2)#linea de corte
  
    # recorte
    recorte = frame[y1:y2, x1:x2]

    # preprocesamiento de la zona de interes
    mb = np.matrix(recorte[:, :, 0])
    mg = np.matrix(recorte[:, :, 1])
    mr = np.matrix(recorte[:, :, 2])

    # color
    color = cv2.absdiff(mg, mb)

    # binarizamos la imagen
    _, umbral = cv2.threshold(color, 40, 255, cv2.THRESH_BINARY)

    # extraemos los contornos en la zona seleccionada
    contornos, _ = cv2.findContours(umbral, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    # ordenar de mayor a menor
    contornos = sorted(contornos, key=lambda x: cv2.contourArea(x), reverse=True)

    # dibujamos los contornos extraidos
    cont=0
    for contorno in contornos:
        area = cv2.contourArea(contorno)
        
        
        
        if area > 500 and area < 50000:
            # detectamos la placa
            x, y, ancho, alto = cv2.boundingRect(contorno)
            
            
             # Extraemos las cordenadas
            xpi = x + x1  # cordenadas en x inicial
            ypi = y + y1  # cordenadas en y inicial

            xpf = x + ancho + x1  # cordenadas en x final
            ypf = y + alto + y1  # cordenadas en y final

            # dibujamos el rectangulo
            cv2.rectangle(frame, (xpi, ypi), (xpf, ypf), (255, 255, 0), 2)
            rango_ypf = (y1, y2)

            if ypi== 360:
                if condicion:
                 tomar_foto(frame, output_folder)
                 condicion=False
                 print("xpi", xpi)
                 print("xpf",xpf)
                 print("ypi", ypi)
                 print("ypf", ypf)
                 print("x1", x1)
                 print("x2",x2)
                 print("y1", y1)
                 print("y2", y2)
                 print("x", x)
                 print("y",y)
                 

                

     
 
            # extraemos los pixeles
            placa = frame[ypi:ypf, xpi:xpf]

            # if ypf or ypi ==y1 :
               
            #    if condicion:
            #     condicion=False
            #     tomar_foto(frame, output_folder)
            #     detector=False
            #     print(area)
            #     print("¡La parte inferior del rectángulo azul pasó por la parte superior del rectángulo verde!")

            # extraemos el ancho y el alto de los fotogramas
            alp, anp, cp = placa.shape

            # proecesamos los pixeles para extraer los valovers de las placas
            Mva = np.zeros((alp, anp))

            # normalizacion de matrices
            nBp = np.matrix(placa[:, :, 0])
            nGp = np.matrix(placa[:, :, 1])
            nRp = np.matrix(placa[:, :, 2])

            # creacion de mascara
            for col in range(0, alp):
                for fil in range(0, anp):
                    Max = max(nRp[col, fil], nGp[col, fil], nBp[col, fil])
                    Mva[col, fil] = 255 - Max
            # binarizacion de la imagen
            _, bin = cv2.threshold(Mva, 150, 255, cv2.THRESH_BINARY)

            # se comvuerta la matriz en una imagen
            bin = bin.reshape(alp, anp)
            bin = Image.fromarray(bin)
            bin = bin.convert("L")

            
            cv2.imshow("placa", placa)

           
                

            # especificamos un tamaño para la placa 
            if alp >= 35 and anp >= 85:
            #     if condicion:
            #         tomar_foto(frame, output_folder)
            #         condicion = False  # Dejar de tomar más fotos una vez que se cumpla la condición
            #         print("Se está tomando la foto")
                # ruta tesseract
                pytesseract.pytesseract.tesseract_cmd = r'C:\Users\luis.acevedo\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
                # parametros tesseract
                config = "--oem 1 --psm 6 "
                texto = pytesseract.image_to_string(bin, config=config)
                # Definir los caracteres a omitir
                caracteres_a_omitir = "!@#$%^&*()_+{}[]|\:;<>?,./?¡""''¥=¿~~~~????"
                texto = ''.join(c for c in texto if c not in caracteres_a_omitir)

                if len(texto) == 7 and texto[
                    0] == "A" or "B" or "C" or "D" or "E" or "F" or "G" or "H" or "I" or "J" or "K" or "L" or "M" or "N" or "O" or "P" or "Q" or "R" or "S" or "T" or "U" or "V" or "W" or "X" or "Y" or "Z" and \
                        texto[
                            1] == "A" or "B" or "C" or "D" or "E" or "F" or "G" or "H" or "I" or "J" or "K" or "L" or "M" or "N" or "O" or "P" or "Q" or "R" or "S" or "T" or "U" or "V" or "W" or "X" or "Y" or "Z" and \
                        texto[
                            2] == "A" or "B" or "C" or "D" or "E" or "F" or "G" or "H" or "I" or "J" or "K" or "L" or "M" or "N" or "O" or "P" or "Q" or "R" or "S" or "T" or "U" or "V" or "W" or "X" or "Y" or "Z" and \
                        texto[3] == " " and texto[0, 1, 2, 4, 5, 6] != " ":
                    Ctexto = texto
                    lista.append(texto)

               

                break
            
            break
      
    # mostrar recorte gris
    cv2.imshow('vehiculos', frame)

    # leer una tecla para salir
    t = cv2.waitKey(1)

    if t == 27 :
        break

# Imprimir la imagen
#bin.show()

resul = eliminar_salto_de_linea(lista)
opplacas = validar_elementos_lista(resul)

for i in opplacas:

    valor_mas_repetido = max(opplacas, key=lambda x: opplacas.count(x))
    repeticiones = opplacas.count(valor_mas_repetido)
print("Posible Placa", valor_mas_repetido)


#print(opplacas)
#print("repeticiones", repeticiones)

#print(valor_mas_repetido)
cap.release()
cv2.destroyAllWindows()
