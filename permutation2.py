# ! /usr/bin/env python
# -*- coding: utf-8 -*-

#Author Παναγιώτης Πράττης/Panagiotis Prattis

'''
A program that accepts two integers n and k as inputs and prints the permutation of [n] 
which is at position k in the lexicographic order of all its permutations of [n].
'''

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
m=[]
m1=[]
m2=[]

n = int(input ("Give number for permutation length: "))
print(n)

for i in range(n):
    m.append(i+1)
    m1.append(i+1)
   
k = int(input ("Give permutation's rank: "))
print(k)

while m:
    f = factorial(len(m) - 1)
    idx, k = divmod(k, f)
    m2.append(m.pop(idx))
assert k == 0 

print("The permutation is this:")
print(m1)
print(m2)


