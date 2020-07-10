import random

SpiSok_1=[]
SpiSok_2=[]
SpiSok_3=[]

for i in range(20):
    SpiSok_1.append(random.randint(-5,5))

for i in SpiSok_1:
    if SpiSok_1[i]<0:
        SpiSok_2.append(SpiSok_1[i])
    elif SpiSok_1[i]>0:
        SpiSok_3.append(SpiSok_1[i])
    else:
        continue



print(SpiSok_1)
print(SpiSok_2)
print(SpiSok_3)