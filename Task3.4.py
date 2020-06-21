radius=int(input("Enter radius: "))
area=int(input("Enter square hall: "))
least_K=int(input("Enter least K from the wall: "))

side=area**0.5

if (side>=2*radius+2*least_K):
    print("Possibly")
else:
    print("Inpossibly")
