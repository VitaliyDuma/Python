tup_1=tuple(input("Enter tuple: "))

lis_1=list(tup_1)
lis_2=[]
lis_3=[]
lis_4=[]

for i in lis_1:
    c=ord(i)
    if (65<=c<=90) or (97<=c<=122):
        lis_2.append(i)
    elif 48<=c<=57:
        lis_3.append(i)
    else:
        lis_4.append(i)

tup_2=tuple(lis_2)
tup_3=tuple(lis_3)
tup_4=tuple(lis_4)


print("Letters: ",tup_2)
print("Numbers: ",tup_3)
print("Special signs: ",tup_4)



