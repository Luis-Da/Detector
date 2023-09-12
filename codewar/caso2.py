""" Escriba la función bmi que calcula el índice de masa corporal (bmi = peso / altura 2 ).

si bmi <= 18.5 devuelve "Bajo peso"

si bmi <= 25.0 devuelve "Normal"

si bmi <= 30.0 devuelve "Sobrepeso"

si bmi > 30 devolver "Obeso"

 """

def bmi(weight, height):
    result=weight/height**2
    if result <= 18.5:
        return "Underweight"
    elif result <=25.0:
        return "Normal"
    elif result  <= 30.0 :
        return "Overweight"
    else :
        return "Obese"
        
    
