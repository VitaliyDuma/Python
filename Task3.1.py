year=int(input("Enter the year:"))

if year%4==0:
    print("year isintercalary")
else:
        print ("year not isintercalary")

century=year/100
print("Century is ",int(century))