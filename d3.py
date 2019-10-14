# ! /usr/bin/env python
# -*- coding: utf-8 -*-

import random

'''
Π15120 Παναγιώτης Πράττης
Η εργασία δημιουργεί μια μετάθεση η οποία έχει τυχαίο μήκος n, κάνοντας ανακάτεμα
μια λίστας με αριθμούς απο 1 έως n και στην συνέχεια υπολογίζει και εμφανίζει
το rank της μετάθεσης στην λεξικογραφική διάταξη
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
print("Θα δημιουργηθεί μια μετάθεση τυχαίου μήκους.")
m1=[]
m2=[]

l = random.randint(5,15)
print("Το μήκος της μετάθεσης ειναι: ", l)
for i in range(l):
    m1.append(i+1)
    m2.append(i+1)
  
random.shuffle(m2)
print("Η μετάθεση είναι η εξής:")
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

print("Προηγούνται της μετάθεσης τόσες μεταθέσεις:")
print(rank)

print("Το rank της μετάθεσης στην λεξικογραφική διάταξη είναι:")
print(rank + 1)

    
    

