# Creación de funciones
# Uso funciones de otras personas 

from functools import reduce
import math
import random

def suma(a,b):
    """Docstring"""
    return(a+b)

def suma(*args):
    return(reduce((lambda a,b:a+b),*args))


def n_random_nums_list(n):
   return [(random.randint(1,100)) for i in range(n)]
     
l = n_random_nums_list(10)
print(l)
print(suma(l))


#  