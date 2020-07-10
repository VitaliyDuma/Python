import random

rand_1=[]
rand_2=[]
rand_3=[]

for i in range(5):
    rand_1.append(random.randint(0,100))

for i in range(5):
    number=int(input("Enter number: "))
    rand_2.append(number)

for i in range(5):
    values=rand_1[i]+rand_2[i]
    rand_3.append(values)
print("List 1: ",rand_1)
print("List 2: ",rand_2)
print("List 3: ",rand_3)