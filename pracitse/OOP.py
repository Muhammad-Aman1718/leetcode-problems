class Solution:
    def check_elements(self, a: list[int], d: int):
        # Your code goes here
        # arr.sort()
        # count = 0
        # for i in b:
        #     if i in a:
        #         count += 1
        #         a.remove(i)

        # if count == len(b):
        #     return True
        # return False

        for i in range(d):
            a.insert(len(a), a[0])
            a.pop(0)
        return a


obj = Solution()
a = [-1, -2, -3, 4, 5, 6, 7]
d = 2
print(obj.check_elements(a, d))
