# Frequencies in a Limited Array


# You are given an array arr[] containing positive integers. The elements in the array arr[] range from  1 to n (where n is the size of the array), and some numbers may be repeated or absent. Your have to count the frequency of all numbers in the range 1 to n and return an array of size n such that result[i] represents the frequency of the number i (1-based indexing).

# Examples:

# Input: arr[] = [2, 3, 2, 3, 5]
# Output: [0, 2, 2, 0, 1]
# Explanation: We have: 1 occurring 0 times, 2 occurring 2 times, 3 occurring 2 times, 4 occurring 0 times, and 5 occurring 1 time.

# Input: arr[] = [3, 3, 3, 3]
# Output: [0, 0, 4, 0]
# Explanation: We have: 1 occurring 0 times, 2 occurring 0 times, 3 occurring 4 times, and 4 occurring 0 times.

# Input: arr[] = [1]
# Output: [1]
# Explanation: We have: 1 occurring 1 time, and there are no other numbers between 1 and the size of the array.


class Solution:
    def frequencyCount(self, arr: list[int]):
        #  code here
        # array: list[int] = []
        # frequency = 0
        # for i in range(1, len(arr) + 1):
        #     if i in arr:
        #         frequency = arr.count(i)
        #         print("This is number i ", i)
        #         print("frequency", frequency)
        #     if i not in arr:
        #         frequency = 0
        #     array.append(frequency)
        # return array
        
        # CHAT GPT SOLUTION
        
        freq = {}

        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        # step 2: build result array
        result = []
        for i in range(1, len(arr) + 1):
            result.append(freq.get(i, 0))  # agar i na ho to 0

        return result


obj = Solution()
# arr = [2, 3, 2, 3, 5]
arr = [3, 3, 3, 3]

print(obj.frequencyCount(arr))
