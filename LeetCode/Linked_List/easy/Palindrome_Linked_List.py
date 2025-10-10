# Palindrome Linked List

# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.


# Example 1:

# Input: head = [1,2,2,1]
# Output: true

# Example 2:


# Input: head = [1,2]
# Output: false


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: reverse second half
        prev = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Step 3: compare
        left = head
        right = prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True

obj = Solution()
head = [1, 2, 2, 1]
print(obj.isPalindrome(head))
