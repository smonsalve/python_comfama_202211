# Ejercicio 61
"""
Computar el promedio de una coleccion de valores ingresada por el usuario. 
El usuario ingresará 0 como valor de sentinela indicando que no habŕan mas valores.
Mostrar el apropiado mensaje de error si el valor ingresado por el usuario es 0
 (El 0 no debe ser usado en el promedio ya que es el centinela)

In this exercise you will create a program that computes the average of a collection
of values entered by the user. The user will enter 0 as a sentinel value to indicate
that no further values will be provided. Your program should display an appropriate
error message if the first value entered by the user is 0.
Hint: Because the 0 marks the end of the input it should not be included in the
average.

"""

values = []
while(True):
    n = float(input(" Ingrese valores a promediar, para terminar ingrese 0\n"))
    if(n==0): 
        break
    else:
        values.append(n)

if(len(values)!=0):
    average = 0
    for v in values:
        average+=v
    print(average/len(values))
else:
    print("La longitud de la coleccion no puede ser 0")

