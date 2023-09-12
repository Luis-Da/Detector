#segun el desarrollo anterior solicitar la estatura y mostrar  el promedio de los hombres y las mujeres
#Luis David Acevedo


# Enunciado anterior:
# De una encuesta que se le realizó a un grupo de N personas en la ciudad de
# Medellín se tienen los siguientes datos: nombre, sexo (M-Masculino, F-femenino),
# salario y nivel de educación (1-primaria, 2-secundaria o 3-profesional). Haga un
# programa para procesar los datos de dicha encuesta e imprima:
# - Porcentaje de hombres y de mujeres con nivel de educación primaria que
# ganan más del salario mínimo
# - Porcentaje de mujeres con nivel de educación profesional que ganan
# menos de dos salarios mínimos.
# - Salario promedio de los hombres y salario promedio de las mujeres
cMasculino=0
cFemenino=0
salarioMin=1000000
estM=0
estF=0

c1=0 #contador hombres con primaria que ganan mas del salario minimo
c2=0 #contador mujeres con primaria que ganan mas del salario minimo

c3=0 #contador mujeres con profesional que ganan menos de dos salarios minimos
cantidad=int(input("Ingrese la cantidad de personas a encuestar: "))

salarioM=0
salarioF=0

for i in range(cantidad):

    nombre=input("Ingrese el nombre: ")

    sexo=input("Ingrese el sexo: M para Masculino, F para Femenino: ")
    if sexo == "M" or sexo=="m":
        cMasculino= cMasculino +1
    elif sexo== "F" or sexo =="f" :
        cFemenino= cFemenino +1
    else:
        print("Error")


    salario=float(input("Ingrese el salario en pesos: "))

    if sexo == "M" or sexo=="m":
        salarioM= salarioM+salario

    if sexo== "F" or sexo =="f":
        salarioF= salarioF+salario

    nivel=int(input("Escriba su nivel de educación: 1 para primaria, 2 para secundaria o 3 para profesional: "))

    if sexo == "M" or sexo=="m" and nivel =="1" and salario>salarioMin:
        c1=c1+1
    
    if sexo== "F" or sexo =="f" and nivel =="1" and salario>salarioMin:
        c2=c2+1
        
    if sexo== "F" or sexo =="f" and nivel =="3" and salario<=salarioMin*2:
        c3=c3+1
    estatura=float(input("ingrese la estatura en centimetros: "))

    if sexo == "M" or sexo=="m":
        estM= estatura+estM

    if sexo== "F" or sexo =="f":
        estF= estatura+estF
    
r1=(c1/cMasculino)*100
r2=(c2/cFemenino)*100

r3=(c3/cFemenino)*100

r4=(salarioM/cMasculino)
r5=(salarioF/cFemenino)

peM=estM/cMasculino
peF=estF/cFemenino

print()
print("El Porcentaje de hombres y de mujeres  con nivel de educación primaria que ganan más del salario mínimo es:{}, {} porciento respectivamente".format(r1,r2))

print("El Porcentaje de mujeres con nivel de educación profesional que ganan menos de dos salarios mínimos es: {}%".format(r3))

print("Salario promedio de los hombres y salario promedio de las mujeres es:{}, {} pesos respectivamente".format(r4,r5))

print("el promedio  de estatura en centimetros de los hombres es {} cm y de las mujeres{} cm ".format(peM,peF))