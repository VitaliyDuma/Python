place=int(input("Enter the number of your seat on the train: "))

if (place<=0) or (place>53):
    print("Incorect date")
else:
    if place%2==0:
        print("place on top")
    else:
        print("place bottom")
    if place>35:
        print("place in side")
    else:
        print("place in conpartment ")

