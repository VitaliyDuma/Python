a=input("Enter string: ")
b=[]
for i in a:
    c=ord(i)
    if (69<=c<=90) or (101<=c<=122):
        b.append(chr(c-4))
    elif (65<=c<69) or (97<=c<101): 
        if c==65:
            c=87
        elif c==66:
            c=88
        elif c==67:
            c=89
        elif c==68:
            c=90
        elif c==97:
            c=119
        elif c==98:
            c=120
        elif c==99:
            c=121
        elif c==100:
            c=122
        b.append(chr(c))
    else:
        b.append(i)
b=''.join(b)
print(b)