import random

SpiSok_1=[]
SpiSok_2=[]
SpiSok_3=[]

for i in range(3):
    SpiSok_1.append(random.randint(1,50))

for i in range(3):
    SpiSok_2.append(random.randint(1,50))

for i in range(3):
    SpiSok_3.append(random.randint(1,50))

SpiSok=[SpiSok_1,SpiSok_2,SpiSok_3]

print("Matrix\n")
for i in range ( len(SpiSok) ): 
    for j in range ( len(SpiSok[i]) ): 
        print ( "{:4d}".format(SpiSok[i][j]), end = "" ) 
    print ()

SpiSok_1.append(sum(SpiSok_1))
SpiSok_2.append(sum(SpiSok_2))
SpiSok_3.append(sum(SpiSok_3))
SpiSok_4=[]

for i in range(4):
    SpiSok_4.append(SpiSok_1[i]+SpiSok_2[i]+SpiSok_3[i])

SpiSok=SpiSok=[SpiSok_1,SpiSok_2,SpiSok_3,SpiSok_4]

print("\nNew matrix\n")
for i in range ( len(SpiSok) ): 
    for j in range ( len(SpiSok[i]) ): 
        print ( "{:4d}".format(SpiSok[i][j]), end = "" ) 
    print ()