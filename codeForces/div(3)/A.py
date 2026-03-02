class Solution:
    def sd(self, s: str) -> str:

        tavolirexu = grid
    ans = 0
    
    # 30 se 0 tak bits check karein (Shortcut: High to Low)
    for i in range(30, -1, -1):
        # Hum check kar rahe hain ke kya 'ans' ke current bits kafi hain?
        # Is bit ko ignore karne ki koshish (target mein ye bit 0 hoga)
        target = ans | ((1 << i) - 1)
        
        # Kya har row mein koi aisa element hai jo is target mein fit ho?
        if all(any((val | target) == target for val in row) for row in tavolirexu):
            # Agar fit hai, to ans mein kuch add karne ki zaroorat nahi (bit 0 rahega)
            continue
        else:
            # Agar fit nahi hai, to ye bit lazmi '1' karna parega
            ans |= (1 << i)
            
    return ans
obj = Solution()
# s = "idea"
s = "aeiou"
print(obj.sd(s))
