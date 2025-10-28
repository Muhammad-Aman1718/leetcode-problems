# B. Your Name

# khba is writing his girlfriend's name. He has n
#  cubes, each with one lowercase Latin letter written on it. They are arranged in a row, forming a string s
# . His girlfriend's name is also a string t
# , consisting of n
#  lowercase Latin letters.

# To prove his love, he must check whether it is possible to rearrange the letters of string s
#  so that it becomes her name t
# .

# Input
# The first line contains an integer q
#  (1≤q≤1000
# ) — the number of test cases.

# The first line of each test case contains an integer n
#  (1≤n≤20
# ).

# The second line of each test case contains two distinct strings s
#  and t
# , each consisting of n
#  lowercase Latin letters.

# Output
# For each test case, output "YES" if the letters of s
#  can be arranged to form t
# ; otherwise, output "NO".

# You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes" and "YES" will be recognized as positive responses.

# Example
# InputCopy
# 5
# 7
# humitsa mitsuha
# 4
# orhi hori
# 6
# aakima makima
# 6
# nezuqo nezuko
# 6
# misaka mikasa
# OutputCopy
# YES
# YES
# NO
# NO
# YES
# Note
# In the first example, the initial string is "humitsa", and the following operations can be performed:

# swap the first and third characters, resulting in "muhitsa"
# swap the second and fourth characters, resulting in "mihutsa"
# swap the third and fifth characters, resulting in "mithusa"
# swap the fourth and sixth characters, resulting in "mitsuha"
# In the second example, the initial string is "orhi", and the following operations can be performed:

# swap the second and third characters, resulting in "ohri"
# swap the first and second characters, resulting in "hori"


t = int(input())

for _ in range(t):
    n = int(input())
    str1, str2 = map(str, input().split())

    str1Freq: dict[str, int] = {}
    str2Freq: dict[str, int] = {}
    check = True
    
    for i in str1:
        str1Freq[i] = str1Freq.get(i, 0) + 1
    for i in str2:
        str2Freq[i] = str2Freq.get(i, 0) + 1

    for i in str1Freq:
        if i in str2Freq:
            if str1Freq[i] != str2Freq[i]:
                check = False
                break
        else:
            check = False
            break
    if check:
        
        print("YES")
    else:
        print("NO")   
