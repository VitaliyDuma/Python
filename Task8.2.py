def bankCalc(n,year):
    if year==1:
        return n+n*0.1
    else:
        year-=1
        sum=bankCalc(n,year)*0.1
        return bankCalc(n,year)+sum
    

n=int(input("Enter money: "))
year=int(input("Enter the number of years: "))

print ("Your money: ",bankCalc(n,year))