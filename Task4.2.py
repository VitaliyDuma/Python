list_a=[]
couter=0
while (couter<10):
    a=int(input("Enter number: "))
    list_a.append(a)
    couter+=1
#print(list_a)
couter_2=0
for i in list_a:
    if i%5==0:
        couter_2+=1
print("The number of numbers divisible by 5: ",couter_2)