# A. Game of Division

# You are given an array of integers a1,a2,…,an
#  of length n
#  and an integer k
# .

# Two players are playing a game. The first player chooses an index 1≤i≤n
# . Then the second player chooses a different index 1≤j≤n,i≠j
# . The first player wins if |ai−aj|
#  is not divisible by k
# . Otherwise, the second player wins.

# We play as the first player. Determine whether it is possible to win, and if so, which index i
#  should be chosen.

# The absolute value of a number x
#  is denoted by |x|
#  and is equal to x
#  if x≥0
# , and −x
#  otherwise.

# Input
# Each test contains multiple test cases. The first line of input contains a single integer t
#  (1≤t≤100
# ) — the number of test cases. The description of the test cases follows.

# The first line of each test case contains two integers n
#  and k
#  (1≤n≤100
# ; 1≤k≤100
# ) — the length of the array and the number k
# .

# The second line of each test case contains n
#  integers a1,a2,…,an
#  (1≤ai≤100
# ) — the elements of the array a
# .

# Output
# For each test case, if it is impossible for the first player to win, print "NO" (without quotes).

# Otherwise, print "YES" (without quotes) and on the next line the appropriate index 1≤i≤n
# . If there are multiple solutions, print any of them.

# You can output each letter in any case (lowercase or uppercase). For example, the strings "yEs", "yes", "Yes" and "YES" will be recognized as a positive answer.

# Example
# Input
# 7
# 3 2
# 1 2 3
# 4 2
# 1 2 4 5
# 5 3
# 10 7 3 4 5
# 5 3
# 1 31 15 55 36
# 2 1
# 17 17
# 2 2
# 17 18
# 1 3
# 6
# Output
# YES
# 2
# NO
# YES
# 3
# NO
# NO
# YES
# 2
# YES
# 1
# Note
# In the first test case, the first player can choose a2=2
# . Then:

# If the second player chooses a1=1
# , the resulting difference is |2−1|=1
#  which is not divisible by k=2
# .
# If the second player chooses a3=3
# , the resulting difference is |2−3|=1
#  which is not divisible by k=2
# .
# In the second test case:

# If the first player chooses a1=1
#  and then the second player chooses a4=5
# , the resulting difference is |1−5|=4
#  which is divisible by k=2
# .
# If the first player chooses a2=2
#  and then the second player chooses a3=4
# , the resulting difference is |2−4|=2
#  which is divisible by k=2
# .
# If the first player chooses a3=4
#  and then the second player chooses a2=2
# , the resulting difference is |4−2|=2
#  which is divisible by k=2
# .
# If the first player chooses a4=5
#  and then the second player chooses a1=1
# , the resulting difference is |5−1|=4
#  which is divisible by k=2
# .
# In any case, the second player wins.


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    rems = [x % k for x in a]
    freq: dict[int, int] = {}
    for r in rems:
        freq[r] = freq.get(r, 0) + 1

    # find any index whose remainder occurs exactly once
    found_index = -1
    for i in range(n):
        if freq[rems[i]] == 1:
            found_index = i + 1  # 1-based
            break

    if found_index == -1:
        print("NO")
    else:
        print("YES")
        print(found_index)
