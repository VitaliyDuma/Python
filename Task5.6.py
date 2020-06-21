text_1=input("Enter text: ")
couter_1=0
couter_2=0
for i in text_1:
    c=ord(i)
    if 65<=c<=90:
        couter_1+=1
    elif 97<=c<=122:
        couter_2+=1
print("%-20s%10d"%("Capital letters",couter_1))
print("%-20s%10d"%("Lowercase letters",couter_2))