# ! /usr/bin/env python
# -*- coding: utf-8 -*-

'''
Π15120 Παναγιώτης Πράττης
Η εργασία δέχεται ως είσοδο δυο αριθμούς  n, k και εκτυπώνει
την μετάθεση μ του [n] η οποία έχει rank τον αριθμό k
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

n = int(input ("Δώσε αριθμό μήκους μετάθεσης: "))
print(n)

for i in range(n):
    m.append(i+1)
    m1.append(i+1)
   
k = int(input ("Δώσε rank μετάθεσης: "))
print(k)

while m:
    f = factorial(len(m) - 1)
    idx, k = divmod(k, f)
    m2.append(m.pop(idx))
assert k == 0 

print("Η μετάθεση είναι η εξής:")
print(m1)
print(m2)


