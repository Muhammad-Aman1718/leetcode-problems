# Count Items Matching a Rule

# You are given an array items, where each items[i] = [typei, colori, namei] describes the type, color, and name of the ith item. You are also given a rule represented by two strings, ruleKey and ruleValue.

# The ith item is said to match the rule if one of the following is true:

# ruleKey == "type" and ruleValue == typei.
# ruleKey == "color" and ruleValue == colori.
# ruleKey == "name" and ruleValue == namei.
# Return the number of items that match the given rule.


# Example 1:

# Input: items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], ruleKey = "color", ruleValue = "silver"
# Output: 1
# Explanation: There is only one item matching the given rule, which is ["computer","silver","lenovo"].

# Example 2:

# Input: items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]], ruleKey = "type", ruleValue = "phone"
# Output: 2
# Explanation: There are only two items matching the given rule, which are ["phone","blue","pixel"] and ["phone","gold","iphone"]. Note that the item ["computer","silver","phone"] does not match.


class Solution:
    def countMatches(self, items: list[list[str]], ruleKey: str, ruleValue: str) -> int:

        data: dict[str, list[str]] = {"type": [], "color": [], "name": []}
        itemsTypes: list[str] = ["type", "color", "name"]
        count: int = 0
        for i in items:
            # print(i)
            for n in range(len(i)):
                data[itemsTypes[n]].append(i[n])

        if ruleKey == "type":
            for i in data["type"]:
                if ruleValue == i:
                    count += 1
        elif ruleKey == "color":
            for i in data["color"]:
                if ruleValue == i:
                    count += 1
        else:
            for i in data["name"]:
                if ruleValue == i:
                    count += 1
        return count

        # ChatGPT Solution   

        # mapping = {"type": 0, "color": 1, "name": 2}
        # idx = mapping[ruleKey]
        # return sum(1 for item in items if item[idx] == ruleValue)


obj = Solution()

items = [
    ["phone", "blue", "pixel"],
    ["computer", "silver", "lenovo"],
    ["phone", "gold", "iphone"],
]
ruleKey = "color"
ruleValue = "silver"
print(obj.countMatches(items, ruleKey, ruleValue))
