def normDate(a,b,c):
    if (0<a<31) and ((b==1)or(b==3)or(b==5)or(b==7)or(b==8)or(b==10)or(b==12))and c>0:
        return True
    elif (0<a<30) and ((b==4)or(b==6)or(b==9)or(b==11))and c>0 :
        return True
    elif (0<a<29) and b==2 and c>0:
        return True
    elif a==29 and b==2 and c%4==0 and c>0 and c%100!=0 and  c%400==0:
        return True
    else:
        return False

a=int(input("Enter day: "))
b=int(input("Enter month: "))
c=int(input("Enter year: "))

print("Date is: ",normDate(a,b,c))