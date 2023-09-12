#3 -  Crear la tabla de multiplicar del 1 hasta el 5 ademas solicitarle un número al usuario para que este sea sumado a cada uno de los resultados de la multiplicación:

 

#Tabla de multiplicar del {variable número} sumandole {}:

#---- x --- = resultado

#--- x --- = resultado

#---- x --- = resultado
A=input("ingrese un numero para sumar al resultado ")
A=int(A)
for i in range(1,6):
    print (f"la tabla del {i}")
    for n in range (0,11):
        resultado= i*n
        res=resultado+A
        print(i,"*", n ,"+", A ,"=",res)

