class Solution:
    def check_elements(self, arr: list[int]):

        count = 0
        for i in arr:
            string = str(i)
            if string == string[::-1]:
                count += 1

        if count == len(arr):
            return True
        return False


obj = Solution()

arr = [111, 222, 333, 444, 555]
print(obj.check_elements(arr))
