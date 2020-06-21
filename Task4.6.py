list_a=[]
couter=0
while True:
    a=int(input("Enter number: "))
    if a==0:
        break
    list_a.append(a)
    couter+=1
couter_2=0
couter_3=0
for i in list_a:
    if i>0:
        couter_2+=1
    else:
        couter_3+=1
print("Negativ: ",couter_3/couter*100,"%")
print("Positiv: ",couter_2/couter*100,"%")
