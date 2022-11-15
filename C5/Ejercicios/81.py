# Ejercicio 81: _Hipotenusa
"""
Escriba una funcion que tome la longitudes de los dos lados mas cortos 
de un triangulo rectangulo como parametros y retorne la hipotenusa usando el teorema de pitagoras
incluya una función principal que lea datos de usuario, llame la función e imprima el resultado.

Write a function that takes the lengths of the two shorter sides of a right triangle as
its parameters. Return the hypotenuse of the triangle, computed using Pythagorean
theorem, as the function’s result. Include a main program that reads the lengths of
the shorter sides of a right triangle from the user, uses your function to compute the
length of the hypotenuse, and displays the result.

"""

def hipotenusa(a, b):
    return((a**2 + b**2)**1/2)

if __name__=='__main__':
    lc = int(input("ingrese lado corto: "))
    ll = int(input("ingrese lado largo: "))
    print(hipotenusa(lc,ll))