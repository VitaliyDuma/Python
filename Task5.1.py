a=input("Enter string: ")
b=[]
for i in a:
    c=ord(i)
    if (65<=c<=86) or (97<=c<=118):
        b.append(chr(c+4))
    elif (86<c<=90) or (118<c<=122): 
        if c==87:
            c=65
        elif c==88:
            c=66
        elif c==89:
            c=67
        elif c==90:
            c=68
        elif c==119:
            c=97
        elif c==120:
            c=98
        elif c==121:
            c=99
        elif c==122:
            c=100
        b.append(chr(c))
    else:
        b.append(i)
b=''.join(b)
print(b)