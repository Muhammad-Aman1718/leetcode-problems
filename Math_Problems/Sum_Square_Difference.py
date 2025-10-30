# Sum Square Difference
# Problem 6


sumOfSquare = 0
squareOfSum = 0

for i in range(1, 100 + 1):
    sumOfSquare += i**2
    squareOfSum += i

print((squareOfSum**2) - sumOfSquare)
