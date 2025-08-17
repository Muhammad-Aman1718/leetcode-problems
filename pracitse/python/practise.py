# user_input = input("Enter your String : ")

# cleaned = user_input.replace(" ", "").lower()

# if cleaned == cleaned[::-1]:
#     print("Its palindrome ")
# else:
#     print("error")

# print(cleaned)

# number = int(input("Enter a number: "))

# if number < 2:
#     print(f"{number} is not a prime number.")
# else:
#     is_prime = True
#     print(int(number**0.5))
#     for i in range(2, int(number**0.5)):
#         print("this is i ",i)
#         if number % i == 0:
#             is_prime = False
#             break

#     if is_prime:
#         print(f"{number} is a prime number.")
#     else:
#         print(f"{number} is not a prime number.")


for i in range(1, 51):

    if i > 1:
        isPrime = True

        for num in range(2, int(i**0.5) + 1):
            if i % num == 0:
                isPrime = False
                break
        if isPrime:
            print(i)
