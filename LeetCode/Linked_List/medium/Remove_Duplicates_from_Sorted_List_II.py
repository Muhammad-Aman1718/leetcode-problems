# Remove Duplicates from Sorted List II

# Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

# Example 1:

# Input: head = [1,2,3,3,4,4,5]
# Output: [1,2,5]

# Example 2:

# Input: head = [1,1,1,2,3]
# Output: [2,3]


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        elementsList = []
        curr = head
        while curr:
            elementsList.append(curr.val)
            curr = curr.next

        freq = {}
        for i in elementsList:
            freq[i] = freq.get(i, 0) + 1

        removeDupList = [i for i in elementsList if freq[i] == 1]

        dummy = ListNode(0)
        tail = dummy 

        for val in removeDupList:
            tail.next = ListNode(val)
            tail = tail.next

        return dummy.next
        
        
obj = Solution()
head = [1,2,3,3,4,4,5]
print(obj.deleteDuplicates(head))