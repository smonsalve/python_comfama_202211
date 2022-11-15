import random

"""
Una ruleta tiene 38 espacios en ella. De ellos, 18 son negros, 18 rojos y 2 verdes. Los espacios verdes están numerados como 0 y 00.
Los espacios rojos están numerados: 1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30 32, 34 y 36. 
los demás enteros entre 1 y 36 son los espacios negros. 

Se pueden hacer muchos tipos de apuestas pueden en la ruleta. En el ejercicio solo van a ser cosiderados los siguientes:
• Un solo numero (1 to 36, 0, or 00)
• Rojo vs Negro
• Par vs Impar (no incluye 0 ni 00)
• 1 al 18 vs 19 al 36

Escribe un programa que simule una jugada de la ruleta utilizando el generador de numeros aleatorios de Python.
Imprime el numero ganador de cada jugada y las apuestas que deben ser pagadas. 

Por ejemplo si cae el numero 13 

Paga el 13, 
paga Negro, 
paga Par, 
Paga del 1 al 18
Si cae 0 o 00 debe mostrar paga 0 o paga 00.
"""

reds = [1,3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
blacks = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
ceros = [0,-1]

todos = reds+ceros+blacks
num = random.choice(todos)

if(num == 0):
    print("Paga 0")
elif(num == -1):
    print("Paga 00")   
else: 
    print(f"Paga el {num}")
    if(num in reds):
        print("paga Rojos")
    elif(num in blacks):
        print("Paga Negros")

    if(num > 0 and num < 19):
        print("Paga 1 al 18")
    elif(num>18 and num < 37):
        print("Paga del 19 al 36")

    if(num%2 == 0):
        print("Paga pares")
    else:
        print("Paga impares")