# Count Pairs That Form a Complete Day I

# Given an integer array hours representing times in hours, return an integer denoting the number of pairs i, j where i < j and hours[i] + hours[j] forms a complete day.

# A complete day is defined as a time duration that is an exact multiple of 24 hours.

# For example, 1 day is 24 hours, 2 days is 48 hours, 3 days is 72 hours, and so on.


# Example 1:

# Input: hours = [12,12,30,24,24]

# Output: 2

# Explanation:

# The pairs of indices that form a complete day are (0, 1) and (3, 4).

# Example 2:

# Input: hours = [72,48,24,3]

# Output: 3

# Explanation:

# The pairs of indices that form a complete day are (0, 1), (0, 2), and (1, 2).


class Solution:
    def countCompleteDayPairs(self, hours: list[int]) -> int:

        # count = 0
        # for i in range(len(hours)):
        #     print("this is i iii   ", i)
        #     for n in range(i + 1, len(hours)):
        #         print("this is n   ", n)
        #         print("this is sum  ", hours[i] + hours[n])
        #         if (hours[i] + hours[n]) % 24 == 0:
        #             count += 1

        # return count

        freq: dict[int, int] = {}  # hash table for remainders
        count = 0

        for h in hours:
            rem = h % 24
            complement = (24 - rem) % 24  # handle rem=0 case also

            if complement in freq:
                count += freq[complement]

            # store this remainder in hash table
            freq[rem] = freq.get(rem, 0) + 1

        return count


obj = Solution()
# hours = [12, 12, 30, 24, 24]
hours = [72, 48, 24, 3]
print(obj.countCompleteDayPairs(hours))
