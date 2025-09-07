class Solution:
    def check_elements(self, arr: list[int]):

        # left = int(len(arr) / 2)

        # addLeft = 0
        # addRight = 0

        # print(left)
        # for i in range(left):
        #     addLeft += arr[i]

        # for x in range(left, len(arr)):
        #     print("this is x  ", x)
        #     addRight += arr[x]

        # multiple = addLeft * addRight

        # return multiple

        nagetive: list[int] = []
        positive: list[int] = []
        newArray: list[int] = []

        for i in arr:
            if i >= 0:
                positive.append(i)
            else:
                nagetive.append(i)

        nag = 0
        pos = 0

        for x in range(len(arr)):
            print(x)
            if x % 2 == 0:
                newArray.append(positive[pos])
                pos += 1
            else:
                newArray.append(nagetive[nag])
                nag += 1

        return newArray


obj = Solution()

arr = [-1, 2, -3, 4, -5, 6]
print(obj.check_elements(arr))
