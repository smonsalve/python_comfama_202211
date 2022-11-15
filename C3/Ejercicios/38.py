
#mes = int(input("Por favor ingrese un mes: "))

# dias =""
# if(mes == 1): 
#     dias = 31
# elif(mes == 2): 
#     dias = "28 o 29 días"
# elif(mes == 3): 
#     dias = 31
# elif(mes == 4): 
#     dias = 30
# elif(mes == 5): 
#     dias = 31
# elif(mes == 6): 
#     dias = 30
# elif(mes == 7): 
#     dias = 31
# elif(mes == 8): 
#     dias = 31
# elif(mes == 9): 
#     dias = 30
# elif(mes == 10): 
#     dias = 31
# elif(mes == 11): 
#     dias = 30
# elif(mes == 12): 
#     dias = 31
# else:
#     print("Ingrese un mes valido (1-12): ")

# print(f"El mes {mes} tiene {dias} días")

# Solución Con diccionarios


mes = input("Por favor ingrese un mes: ")

meses = {
    "enero":31,
    "febrero":"28 o 29",
    "marzo":31
}

print(f"El mes {mes.upper()} tiene {meses[mes.lower()]} días")