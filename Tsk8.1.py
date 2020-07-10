def calcul(a,b,c):
    if c=='+':
        return a+b
    elif c=='-':
        return a-b
    elif c=='*':
        return a*b
    elif c=='/':
        if b==0:
            print("Incorect date")
            quit()
        return a/b
    else:
        print("Incorect date")

a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=input("Enter char:")

print("Resalt: ", calcul(a,b,c))