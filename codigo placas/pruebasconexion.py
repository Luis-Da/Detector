import cv2
import numpy as np
import pytesseract
from PIL import Image
from datetime import datetime
import mysql.connector
import os


# Configuración de la conexión a la base de datos
config = {
    'user': 'root',
    'password': 'example',
    'host': 'localhost',  # Utiliza localhost si ejecutas la aplicación Python en la misma máquina que Docker
    'port': 3306,
    'database': 'vehiculos_detectados',
}

# Crear una conexión a la base de datos
connection = mysql.connector.connect(**config)

# Crear un cursor para ejecutar comandos SQL
cursor = connection.cursor()

# Código SQL para insertar un registro en la tabla "vehiculos"
sql_insert = "INSERT INTO vehiculos (placa, ubicacion, fecha, registro) VALUES (%s, %s, %s, %s)"



def tomar_foto(frame, output_folder):
    # Obtener la fecha y hora actual
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d_%H%M%S")
    output_path = f"{output_folder}/foto_capturada_{timestamp}.png"

    cv2.imwrite(output_path, frame)
    #print("Foto de placa capturada:", output_path)
    return output_path


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
video_path= "4placas.mp4"
cap = cv2.VideoCapture( video_path)
lista = []
Ctexto = ""


output_folder = "registro fotografico" #ruta para almacernar las fotos
# Definir la condición para capturar la foto (puedes ajustar esto según tus necesidades)
foto = False#condicion pra toma de  foto
suiche=False#indica el cambio de zona de la placa
imprimir=False# activa la impresion de los resultados
# captura de los fotogramas en el video

while True :
    
    ret, frame,  = cap.read()
    
    if not ret:
        break
    # dibujamos el rectangulo, los fotogramas quedan almacenado en frame
   


    

    # EXTRAEMOS  el ancho , el alto de los fotogramas
    al, an, c = frame.shape

    # tomar centro de imagen
    x1 = int(an / 3)
    x2 = int(x1 * 2)

    y1 = int(al / 3)
    y2 = int(y1 * 2)

    # texto
#roi de salida
    ys1 = int(200)
    ys2 = int(al / 3)



    

    # ubicamos el rectangulo en la zona extraida
    #cv2.rectangle(frame, (x1, y1 ), (x2, y2), (0, 255, 0), 2)
   # cv2.line(frame, (x1, y1+100), (x2, y1+100), (100, 0, 0), 2)#linea de corte

    #roi salida
   # cv2.rectangle(frame, (x1, ys1 ), (x2, ys2), (0, 0, 255), 2)
    # recorte
    recorte = frame[y1:y2, x1:x2]
    salida=frame[ys1:ys2, x1:x2]

    # preprocesamiento de la zona de interes
    mb = np.matrix(recorte[:, :, 0])
    mg = np.matrix(recorte[:, :, 1])
    mr = np.matrix(recorte[:, :, 2])
#salida
    mbs = np.matrix(salida[:, :, 0])
    mgs = np.matrix(salida[:, :, 1])
    mrs = np.matrix(salida[:, :, 2])

    # color
    color = cv2.absdiff(mg, mb)
#salida
    colors=cv2.absdiff(mgs, mbs)

    # binarizamos la imagen
    _, umbral = cv2.threshold(color, 40, 255, cv2.THRESH_BINARY)
#salida
    _, umbrals = cv2.threshold(colors, 40, 255, cv2.THRESH_BINARY)
    # extraemos los contornos en la zona seleccionada
    contornos, _ = cv2.findContours(umbral, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
#salida    
    contornossal, _ = cv2.findContours(umbrals, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    

    # ordenar de mayor a menor
    contornos = sorted(contornos, key=lambda x: cv2.contourArea(x), reverse=True)
#salida
    contornossal = sorted(contornossal, key=lambda x: cv2.contourArea(x), reverse=True)
#salida

    for contorno in contornossal:
        area = cv2.contourArea(contorno)
        
        
        
        if area > 500 and area < 50000 :
            # detectamos la placa
            x, y, ancho, alto = cv2.boundingRect(contorno)
            
            
             # Extraemos las cordenadas
            xpi = x + x1  # cordenadas en x inicial
            ypi = y + ys1  # cordenadas en y inicial

            xpf = x + ancho + x1  # cordenadas en x final
            ypf = y + alto + ys1  # cordenadas en y final
            suiche=True

            # dibujamos el rectangulo
            cv2.rectangle(frame, (xpi, ypi), (xpf, ypf), (255, 255, 0), 2)
            
            if suiche== True:

                
                imprimir=True
                lista = []
                resul = []
             
                # tomar foto
                if foto== True:
                     ruta_imagen_capturada = tomar_foto(frame, output_folder)
                     foto=False
                     print ("Detecccion realizada")
                     

           
            


    # dibujamos los contornos extraidos
    
    for contorno in contornos:
        area = cv2.contourArea(contorno)
        
        
        
        if area > 5000 and area < 50000:
            # detectamos la placa
            x, y, ancho, alto = cv2.boundingRect(contorno)
            
            
             # Extraemos las cordenadas
            xpi = x + x1  # cordenadas en x inicial
            ypi = y + y1  # cordenadas en y inicial

            xpf = x + ancho + x1  # cordenadas en x final
            ypf = y + alto + y1  # cordenadas en y final

            # dibujamos el rectangulo
            cv2.rectangle(frame, (xpi, ypi), (xpf, ypf), (255, 255, 0), 2)
            #imprimir=False
            #print("esta detectando en zona verde")
            

            foto = True

                

     
 
            # extraemos los pixeles
            placa = frame[ypi:ypf, xpi:xpf]

           
               
            
           

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

            

           
                

            # especificamos un tamaño para la placa 
            if alp >= 35 and anp >= 85:
               
           
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
                    
                    lista.append(texto)

                    resul = eliminar_salto_de_linea(lista)
                    opplacas = validar_elementos_lista(resul)

                    for i in opplacas:

                        valor_mas_repetido = max(opplacas, key=lambda x: opplacas.count(x))
                        repeticiones = opplacas.count(valor_mas_repetido)

                    if imprimir == True:    
                        print("Placa identificada: ", valor_mas_repetido)
                        imprimir=False
                        print("buscando nuevo vehiculo")

                    # Validar si hay una placa detectada y guardarla en la base de datos
                        if valor_mas_repetido:
                            ubicacion = "Santa fe de antioquia"  # Puedes ajustar esto según el lugar donde se realiza la detección
                            fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            # Aquí deberías guardar la imagen de la placa en formato BLOB, puedes convertir la imagen a bytes y luego guardarla
                           
                            registro = cv2.imencode('.png', cv2.imread(ruta_imagen_capturada))[1].tobytes()
                            datos_vehiculo = (valor_mas_repetido, ubicacion, fecha, registro)
                            cursor.execute(sql_insert, datos_vehiculo)
                            connection.commit()

                        # Cerrar el cursor y la conexión
                      
                        


               

                break
            
            break
      
    # mostrar recorte gris
    cv2.imshow('vehiculos', frame)

    # leer una tecla para salir
    t = cv2.waitKey(1)

    if t == 27 :
        break


print("Placa identificada:", valor_mas_repetido)

if valor_mas_repetido:
    ubicacion = "Santa fe de antioquia"  #  ajustar esto según el lugar donde se realiza la detección
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            #  guardar la imagen de la placa en formato BLOB,  convertir la imagen a bytes y luego guardarla
                           
    registro = cv2.imencode('.png', cv2.imread(ruta_imagen_capturada))[1].tobytes()
    datos_vehiculo = (valor_mas_repetido, ubicacion, fecha, registro)
    cursor.execute(sql_insert, datos_vehiculo)
    connection.commit()



cap.release()
cv2.destroyAllWindows()


cursor.close()
connection.close()    