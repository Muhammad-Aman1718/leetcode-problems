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


# def fun():
#     s = 2
#     return s

# print(fun())


def fun():

    yield 1
    yield 2
    yield 3
    # return 


for value in fun():
    print(value)
