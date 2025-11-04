# Power Digit Sum

num = 2 ** 1000

numStr = str(num)
total = 0

for i in range(len(str(num))):
    total += int(numStr[i])

print(total)
