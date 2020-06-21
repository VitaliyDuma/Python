import random
rand_A=random.randint(0,100)
couter=0
print(rand_A)
while (couter<=9):
    number=int(input("Enter your number: "))
    if number==rand_A:
        print("You win!!!")
        break
    elif number<rand_A:
        couter+=1
        print("The number is more! Try agan!")
    elif number>rand_A:
        couter+=1
        print("The number is less! Try agan!")     
if couter==10:
    print("You loss!!!!")
