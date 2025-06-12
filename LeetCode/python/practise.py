import math

# # Function to find LCM
# def find_lcm(a, b):
#     if a > b:
#         greater = a
#     else:
#         greater = b

#     while True:
#         if (greater % a == 0) and (greater % b == 0):
#             lcm = greater
#             break
#         greater += 1

#     return lcm


def find_hcf(a: int, b: int) -> int:
    return math.gcd(a, b)


# # User input
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Call function and print result
result = find_hcf(num1, num2)
print("LCM of", num1, "and", num2, "is:", result)
