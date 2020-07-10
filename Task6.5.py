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
SpiSok_1_1=[]
SpiSok_2_2=[]
SpiSok_3_3=[]

SpiSok_1_1.append(SpiSok_1[0])
SpiSok_1_1.append(SpiSok_2[0])
SpiSok_1_1.append(SpiSok_3[0])
SpiSok_2_2.append(SpiSok_1[1])
SpiSok_2_2.append(SpiSok_2[1])
SpiSok_2_2.append(SpiSok_3[1])
SpiSok_3_3.append(SpiSok_1[2])
SpiSok_3_3.append(SpiSok_2[2])
SpiSok_3_3.append(SpiSok_3[2])

SpiSok_4=[min(SpiSok_1_1),min(SpiSok_2_2),min(SpiSok_3_3)]

print("Minimum elements: ",SpiSok_4)
print("The maximum element of the minimum : ",max(SpiSok_4))