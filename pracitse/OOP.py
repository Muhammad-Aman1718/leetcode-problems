class Solution:
    def check_elements(self, arr, n, A, B):
        # Your code goes here
        # arr.sort()
        rangeAB = 0
        count = 0
        for i in range(A, B + 1):
            if i in arr:
                count += 1
            rangeAB += 1

        if count == rangeAB:
            return True
        return False


obj = Solution()
n = 7
A = 2
B = 6
arr = {1, 4, 5, 2, 7, 8, 3}

print(obj.check_elements(arr, n, A, B))
