def is_year_leap(a):
    if a%4==0 and a>0 and (a%100!=0 or  a%400==0):
        return True
    else:
        return False

a=int(input("Enter year: "))
print("Year is leap: ",is_year_leap(a))