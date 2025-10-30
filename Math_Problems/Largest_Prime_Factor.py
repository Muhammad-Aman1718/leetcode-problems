# Largest Prime Factor
# Problem 3

value = 600851475143
arr: list[int] = []
i = 2

while True:
    divide = value / i
    if value % i == 0:
        value = divide
        arr.append(i)
        i = 2
    if value == 1:
        break
    i += 1

print(max(arr))
