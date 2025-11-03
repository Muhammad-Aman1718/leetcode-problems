# Defanging an IP Address

# Given a valid (IPv4) IP address, return a defanged version of that IP address.
# A defanged IP address replaces every period "." with "[.]".

# Example 1:

# Input: address = "1.1.1.1"
# Output: "1[.]1[.]1[.]1"

# Example 2:

# Input: address = "255.100.50.0"
# Output: "255[.]100[.]50[.]0"


class Solution:
    def defangIPaddr(self, address: str) -> str:

        # adr = list(address)
        # for i in range(len(adr)):
        #     if adr[i] == ".":
        #         adr[i] = "[.]"

        # return "".join(adr)

        return address.replace(".", "[.]")


obj = Solution()
address = "1.1.1.1"
print(obj.defangIPaddr(address))
