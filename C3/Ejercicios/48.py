"""
0 Dragon
1 Snake
2 Horse
3 Sheep
4 Monkey
5 Rooster
6 Dog
7 Pig
8 Rat
9 Ox
10 Tiger
11 Hare
"""
year = int(input("Por favor ingrese un año: "))
zodiaco = year%12
animal =""
if(zodiaco == 0): 
    animal = "Dragon"
elif(zodiaco == 1): 
    animal = "Snake"
elif(zodiaco == 2): 
    animal = "Horse"
elif(zodiaco == 3): 
    animal = "Sheep"
elif(zodiaco == 4): 
    animal = "Monkey"
elif(zodiaco == 5): 
    animal = "Rooster"
elif(zodiaco == 6): 
    animal = "Dog"
elif(zodiaco == 7): 
    animal = "Pig"
elif(zodiaco == 8): 
    animal = "Rat"
elif(zodiaco == 9): 
    animal = "Ox"
elif(zodiaco == 10): 
    animal = "Tiger"
elif(zodiaco == 11): 
    animal = "Hare"

print(f"El zodiaco para el año {year} es {animal}")