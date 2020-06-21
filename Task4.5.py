P=int(input("Enter P: "))
H=int(input("Enter H: "))
list_a=[]
while True:
    a=int(input("Enter number: "))
    if (a==P) or (a==H):
        break
    list_a.append(a)
suma=0
for i in list_a:
    suma+=i
if suma>P:
    print("The amount is large!")
else:
    print("The amount is less!")
dobt=0
for i in list_a:
    dobt*=i
if dobt>H:
    print("The product is large!")
else:
    print("The product is less!")
couter=0
for i in list_a:
    if i>=P and i<=H:
        couter+=1
print("The number of numbers included in the interval: ",couter)