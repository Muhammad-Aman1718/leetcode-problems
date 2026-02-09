# Social Experiment

# Right now, the largest social experiment in the history of Codeforces is taking place, involving n
#  people. They are required to form teams of 2−3
#  people, after which each team chooses one of two civilizations to participate in the social experiment.

# The organizers of this social experiment want to know what the possible difference in the number of people in the civilizations could be. Find the minimum possible difference.

# Input
# Each test consists of several test cases. The first line contains a single integer t
#  (1≤t≤104)
#  — the number of test cases. The following lines describe the test cases.

# In the only line of each test case, there is an integer n
#  — the number of people participating in the social experiment (2≤n≤104)
# .

# Output
# For each number n
# , output the minimum possible difference between the number of people in the civilizations.


import sys


def solve():
    # Input read karne ke liye
    try:
        line = sys.stdin.read().split()
        if not line:
            return

        t = int(line[0])  # Test cases
        results = []

        for i in range(1, t + 1):
            n = int(line[i])

            if n == 2:
                results.append("2")
            elif n == 3:
                results.append("3")
            else:
                # n % 2 check karta hai ke remainder kya hai
                # Even ke liye 0, Odd ke liye 1
                results.append(str(n % 2))

        # Ek saath saare answers print karna fast hota hai
        print("\n".join(results))

    except EOFError:
        pass


if __name__ == "__main__":
    solve()
