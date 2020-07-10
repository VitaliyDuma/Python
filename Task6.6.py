SpiSok_1=[]
SpiSok_2=[]
SpiSok_3=[]

for i in range(3):
    SpiSok_1.append(int(input("Enter element matrix №1: ")))

for i in range(3):
    SpiSok_2.append(int(input("Enter element matrix №1: ")))

for i in range(3):
    SpiSok_3.append(int(input("Enter element matrix №1: ")))

matrix_1=[SpiSok_1,SpiSok_2,SpiSok_3]

SpiSok_4=[]
SpiSok_5=[]
SpiSok_6=[]

for i in range(3):
    SpiSok_4.append(int(input("Enter element matrix №2: ")))

for i in range(3):
    SpiSok_5.append(int(input("Enter element matrix №2: ")))

for i in range(3):
    SpiSok_6.append(int(input("Enter element matrix №2: ")))

matrix_2=[SpiSok_4,SpiSok_5,SpiSok_6]

print("\nMatrix 1\n")

for i in range ( len(matrix_1) ): 
    for j in range ( len(matrix_1[i]) ): 
        print ( "{:4d}".format(matrix_1[i][j]), end = "" ) 
    print ()

print("\nMatrix 2\n")

for i in range ( len(matrix_2) ): 
    for j in range ( len(matrix_2[i]) ): 
        print ( "{:4d}".format(matrix_2[i][j]), end = "" ) 
    print ()

matrix_3=[]

for i in range(3):
    matrix_3.append(SpiSok_1[i])
    matrix_3.append(SpiSok_2[i])
    matrix_3.append(SpiSok_3[i])
    matrix_3.append(SpiSok_4[i])
    matrix_3.append(SpiSok_5[i])
    matrix_3.append(SpiSok_6[i])

matrix_3.sort()

SpiSok_7=[matrix_3[-1],matrix_3[-2],matrix_3[-3]]
SpiSok_8=[matrix_3[-4],matrix_3[-5],matrix_3[-6]]
SpiSok_9=[matrix_3[-7],matrix_3[-8],matrix_3[-9]]


matrix_4=[SpiSok_7,SpiSok_8,SpiSok_9]

print("New matrix")

for i in range ( len(matrix_4) ): 
    for j in range ( len(matrix_4[i]) ): 
        print ( "{:4d}".format(matrix_4[i][j]), end = "" ) 
    print ()