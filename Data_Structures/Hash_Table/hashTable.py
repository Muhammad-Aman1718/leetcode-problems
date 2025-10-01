# class MyHashSet:
#     def __init__(self) -> None:
#         self.size = 100
#         # self.table: list[list[int]] = [[] for _ in range(self.size)]
#         self.table: list[list[tuple[int, int]]] = [[] for _ in range(self.size)]
#         print("this is self table    -       -       ->  ", self.table)

#     # def add(self, key: int):
#     #     idx = key % self.size  # Hash Function
#     #     print("this is add idx      -> ", idx)
#     #     if key not in self.table[idx]:
#     #         self.table[idx].append(key)

#     # def contains(self, key: int) -> bool:
#     #     idx = key % self.size
#     #     print("this is contains idx      -> ", idx)
#     #     return key in self.table[idx]

#     def put(self, key: int, value: int) -> None:
#         idx = key % self.size
#         # for i, (k, v) in enumerate(self.table[idx]):
#         #     if k == key:
#         #         self.table[idx][i] = (key, value)
#         #         return
#         self.table[idx].append((key, value))

#     def get(self, key: int) -> int:
#         idx = key % self.size
#         for k, v in self.table[idx]:
#             if k == key:
#                 return v
#         return -1


# obj = MyHashSet()
# # obj.add(10)
# # obj.add(12)
# # obj.add(13)
# # obj.add(14)
# # obj.add(186537)
# # obj.add(1876)
# # obj.add(1876)
# # obj.add(1987)
# # obj.add(17645)
# # obj.add(1875)
# # obj.add(143)
# # obj.add(17654)
# # obj.add(1745)
# # obj.add(17654)
# # obj.add(17645)
# # obj.add(17645)
# # obj.add(1764)
# # obj.add(1876876)
# # obj.add(1654)
# # obj.add(165)
# # obj.add(1876)
# # obj.add(1096)
# # obj.add(1785)
# # obj.add(1765)
# # obj.add(1987)
# # obj.add(19876)
# # obj.add(1876)
# # obj.add(1654)
# # obj.add(187453)
# # obj.add(1876)
# # obj.add(1765)
# # obj.add(1654)
# # obj.add(1876)
# # obj.add(15)
# # obj.add(165)
# # obj.add(187)
# # obj.add(1874)
# # obj.add(147)
# # obj.add(1432)
# # obj.add(1453)
# # obj.add(1443)
# # obj.add(1465)
# # obj.add(1543)
# # obj.add(1543)
# # obj.add(164)
# # obj.add(1654)
# # obj.add(1464)
# # obj.add(165)
# # obj.add(1654)
# # obj.add(1654)
# # obj.add(187)
# # obj.add(1765)
# # obj.add(145)
# # obj.add(4324)
# # obj.add(15463)
# # obj.add(1476)
# # obj.add(132)
# # obj.add(1432)
# # obj.add(1543)
# # obj.add(1423)
# # obj.add(124)
# # obj.add(17)
# # obj.contains(1432)
# # obj.contains(1543)
# # obj.contains(1423)
# # obj.contains(124)
# # obj.contains(17)
# # obj = MyHashSet()


# obj.put(2, 479)
# obj.put(232, 476)
# obj.put(23, 445432)
# obj.put(223454, 4432)
# obj.put(2234544, 4432)
# obj.put(223654, 4432)
# obj.put(2265, 4432)
# obj.put(227654, 443)
# obj.put(227654, 442)

# print(obj.get(2234544))
# print(obj.table)

