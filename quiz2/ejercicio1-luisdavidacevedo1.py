#1 - Solicite 3 números a un usuario y calcule cual de los 3 números es el mayor

print("Ingrese 3 numeros para determinar cual es el mayor")
A=input ("ingrese el primer numero ")
B=input ("ingrese el segundo numero ")
C=input ("ingrese el tercer numero ")

A=int(A)
B=int(B)
C=int(C) 

if A > B  and A>C:
    print (f"El numero {A} es el mayor numero")
elif B> A and B>C :
    print (f"El numero {B} es el mayor numero")
else :
    print (f"El numero {C} es el mayor numero")
