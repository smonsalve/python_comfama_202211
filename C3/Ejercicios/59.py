"""
Ejercicio 59: Es una placa Valida?
Las placas consisten de tres lletras mayusculas seguidas de tres numeros.
cuando todas las placas fueron usadas el formato fue cambiado a cuatro numeros seguido de tres letras mayusculas

Escriba un programa que lea una placa del usuario 
y verifique si es una placa valida del estilo viejo o del nuevo estilo nuevo o no es una placa valida

"""
placa = input("Ingrese una placa:")

def placa_valida(placa):
    if( placa[3:].isnumeric() and placa[:3].isalpha() ):
        print("Placa Vieja Valida")
    elif(placa[:4].isnumeric() and placa[4:].isalpha()):
        print("Placa Nueva Valida")
    else:
        print("Placa no valida")

placa_valida(placa)