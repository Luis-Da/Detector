"""Tengo un gato y un perro.

los conseguí al mismo tiempo que gatito/cachorro. Eso fue humanYearshace años.

Devuelve sus respectivas edades ahora como [ humanYears, catYears, dogYears]

NOTAS:

añoshumanos >= 1
humanYears son solo números enteros
Años del gato
15años de gato para el primer año
+9años de gato por segundo año
+4cat años por cada año después de eso
Años del perro
15años de perro para el primer año
+9años de perro por segundo año
+5años de perro por cada año después de eso """





def human_years_cat_years_dog_years(human_years):
    años_gato = 0
    años_perro = 0
    if type(human_years)== int:
        if human_years >= 1:
            for i in range(human_years):
                if i ==0:
                    años_gato = años_gato + 15
                    años_perro = años_perro + 15
                elif i==1:
                    años_gato = años_gato + 9
                    años_perro = años_perro + 9
                else:
                    años_gato = años_gato + 4
                    años_perro = años_perro + 5
            return [human_years, años_gato, años_perro]
        else:
            return "no es valido"
    else:
         return "no es valido"
    
      