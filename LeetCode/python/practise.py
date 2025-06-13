def primeNum(a: int):

    if (a == 2) or (a == 3):
        return print("this is prime number")

    # isPrime = True
    i = 2

    while i <= a:
        if a / i == 0:
            print(i)
            return print("this is prime number")
        i += 1
        print(a / i , "this is division")
        print(i)

    return print("this number is not prime")


num = int(input("Enter your Number : "))

print(primeNum(num))
