# Exercise 80: Coin Flip Simulation
# Exercicio 81: Simulacion lanzamiento Moneda

"""
What’s the minimum number of times you have to flip a coin before you can have
three consecutive flips that result in the same outcome (either all three are heads or
all three are tails)? What’s the maximum number of flips that might be needed? How
many flips are needed on average? In this exercise we will explore these questions
by creating a program that simulates several series of coin flips.
Create a program that uses Python’s random number generator to simulate flipping
a coin several times. The simulated coin should be fair, meaning that the probability
of heads is equal to the probability of tails. Your program should flip simulated
coins until either 3 consecutive heads of 3 consecutive tails occur. Display an H each
time the outcome is heads, and a T each time the outcome is tails, with all of the
outcomes shown on the same line. Then display the number of flips needed to reach
3 consecutive flips with the same outcome. When your program is run it should
perform the simulation 10 times and report the average number of flips needed.
Sample output is shown below:
"""
from functools import reduce
import random


stats = []
for i in range(10):
    flips = []
    cont = 0
    while(True):
        flips.append(random.randint(0,1))
        if(cont>=3) and (flips[-3]==flips[-2]==flips[-1]): break
        cont+=1
    stats.append(cont)
    print(flips, len(flips), " flips")
print((reduce(lambda a,b:a+b,stats)/10))

