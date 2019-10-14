# ! /usr/bin/env python
# -*- coding: utf-8 -*-

#Author Παναγιώτης Πράττης/Panagiotis Prattis

'''
A program that accepts as an input a permutation in a list format from natural numbers 
separated by the space character (eg 7 10 9 11 2 1 3 5 6 8 4) 
and prints the permutation rank in the lexicographic order of all same length permutations.
'''

import random


def factorial(number):
    if (number == 0):
        f = 1
        return f
    else:
        f = 1
        while (number != 0):
            f = f*number
            number = number - 1
        return f


#Main
print("A random length permutation will be created.")
m1=[]
m2=[]

l = random.randint(5,15)
print("Permutation's length is: ", l)
for i in range(l):
    m1.append(i+1)
    m2.append(i+1)
  
random.shuffle(m2)
print("Permutation is this:")
print(m1)
print(m2)

a = []
for i in range(0,l):
    if (i != l):
        num = 0
        for j in range(i, l):
            if (m2[i] > m2[j]):
                num = num + 1
        a.append(num)
    else:
        a.append(0)

rank = 0
f = l
for i in range(0,l):
    rank = rank + a[i]*factorial(f-1)
    f = f - 1

print("There are so many permutations preceding the permutation:")
print(rank)

print("The rank of the permutation in the lexicographic order is:")
print(rank + 1)

    
    

