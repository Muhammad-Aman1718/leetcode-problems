# A. Legs

# It's another beautiful day on Farmer John's farm.

# After Farmer John arrived at his farm, he counted n
#  legs. It is known only chickens and cows live on the farm, and a chicken has 2
#  legs while a cow has 4
# .

# What is the minimum number of animals Farmer John can have on his farm assuming he counted the legs of all animals?

# Input
# The first line contains single integer t
#  (1≤t≤103
# ) — the number of test cases.

# Each test case contains an integer n
#  (2≤n≤2⋅103
# , n
#  is even).

# Output
# For each test case, output an integer, the minimum number of animals Farmer John can have on his farm.

# Example
# Input
# 3
# 2
# 6
# 8
# Output
# 1
# 2
# 2


t = int(input())

for _ in range(t):
    n = int(input())

    cowLegs = n // 4
    remainingLegs = n % 4
    checkenLegs = remainingLegs // 2
    print(cowLegs + checkenLegs)
