import random

SpiSok_1=[]
SpiSok_2=[]

for i in range(10):
    SpiSok_1.append(random.randint(0,9))

couter=0

for i in SpiSok_1:
    if i%2==0:
        SpiSok_2.append(couter)
    couter+=1
    

print("List: ",SpiSok_1)
print("Index: ",SpiSok_2)