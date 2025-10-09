class Solution:
    def is_possible_to_get_seats(self, arr: list[int]) -> bool:
        # code here
        result = []
        freq: dict[int, int] = {}
        for i in arr:
            freq[i] = freq.get(i, 0) + 1
        print(freq)
        t = max(freq.values())
        print(t)
        for i in freq:
            if freq[i] == t:
                result.append(i)
        return min(result)


obj = Solution()
seats = [2, 2, 1, 1, 0, 0, ]

print(obj.is_possible_to_get_seats(seats))
