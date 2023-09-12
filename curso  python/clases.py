
#en el primer parametro es para la pocicion de la lista dentro del arreglo multidimensional
# el segundo parametro es para la pocicion dentro de la lista antes seleccionada

#una clase permite guardar variables y funciones, funciones ->metodos, variables->parametros, propiedades
 #una instancia de una clase se denomina objeto

class cuadrado:
    def __init__(self, ancho, alto): #self hace referencia a esta misnma clase, esta funcion es la funcion constructora
        self.ancho= ancho
        self.alto= alto

    def calcularArea(self):
        area=self.ancho*self.alto 
        return area   

figura= cuadrado(10,12)

print(figura.alto)


print(figura.calcularArea())





class persona:
    def __init__(self, nombre, apellido, dni, telefono): #los parametros de la funcion constructora son las variables de entrada
        self.nombre= nombre
        self.apellido= apellido
        self.dni= dni
        self.telefono= telefono

class empleado:
    def __init__(self, nombre, apellido, dni, telefono, salario): #los parametros de la funcion constructora son las variables de entrada
        self.nombre= nombre
        self.apellido= apellido
        self.dni= dni
        self.telefono= telefono
        self.salario


emp=empleado("lucas", "moy", "12345", "3103559022", 10000000000000)


#cliente puede pertecer a la clase persona, entonces puede herredar sus propiedades

class cliente(persona):
    def __init__(self, nombre, apellido, dni, telefono, salario):
        super().__init__(nombre, apellido, dni, telefono)
        self.salario

#el debido proceso es crear cada clase en un archivo distinto e importrlo a donde se necesite con el codigo
# #from Name_del_archivo import name_dela_clase
# 
# hosting profesionales: google, amazon, azure, ibm        


