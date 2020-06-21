cash=int(input("Enter you cash: "))
if cash<=0:
     print("Incorect date")
else:
    if cash>=200:
        K_200=int(cash/200)
        K_100=int((cash%200)/100)
        K_50=int(((cash%200)%100)/50)
        K_10=int((((cash%200)%100)%50)/10)
        K_1=int((((cash%200)%100)%50)%10)
    elif (cash<200) and (cash>=100):
        K_200=0
        K_100=int((cash%200)/100)
        K_50=int(((cash%200)%100)/50)
        K_10=int((((cash%200)%100)%50)/10)
        K_1=int((((cash%200)%100)%50)%10)
    elif (cash<100) and (cash>=50):
        K_200=0
        K_100=0
        K_50=int(((cash%200)%100)/50)
        K_10=int((((cash%200)%100)%50)/10)
        K_1=int((((cash%200)%100)%50)%10)
    elif (cash<50) and (cash>=10):
        K_200=0
        K_100=0
        K_50=0
        K_10=int((((cash%200)%100)%50)/10)
        K_1=int((((cash%200)%100)%50)%10)
    elif (cash<10) and (cash>=1):
        K_200=0
        K_100=0
        K_50=0
        K_10=0
        K_1=int((((cash%200)%100)%50)%10)

    print("Banknots 200: ",K_200)
    print("Banknots 100: ",K_100)
    print("Banknots 50: ",K_50)
    print("Banknots 10: ",K_10)
    print("Banknots 1: ",K_1)