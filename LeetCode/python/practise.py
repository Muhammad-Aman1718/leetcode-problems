# Prime number finder
# def primeNum(a: int):

#     if (a == 2) or (a == 3):
#         return print("this is prime number")
#     i = 2
#     while i <= a:
#         if a / i == 1:
#             return print("this is prime number")
#         if a % i == 0:
#             return print("this is not prime number")
#         i += 1

# num = int(input("Enter your Number : "))
# print(primeNum(num))


a = int(input("Enter your number : "))

match a:
    case 1:
        print("one")
    case 2:
        print("two")
    case 3:
        print("three")
    case _:
        print("other number")
