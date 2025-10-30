# Even Fibonacci Numbers

arr = [1, 2]
i = 2
maxValue = 0
evenValuedSum = 0
while maxValue < 4000000:
    arr.append(arr[i - 2] + arr[i - 1])
    maxValue = arr[i - 2] + arr[i - 1]
    i += 1

for i in arr:
    if i % 2 == 0:
        evenValuedSum += i

print(arr)
print(evenValuedSum)
