import math

def is_prime(number):
    if number < 2:
        print("A number must be 2 and more")
        quit()
    i = 2
    count = int(math.sqrt(number))

    while i <= count:
        if number % i == 0:
            print("This is composite number")
            return False
        i += 1
    return True


number = int(input("Enter the number: "))
print("Number is prime? :",is_prime(number))