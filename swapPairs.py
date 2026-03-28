#Leetcode 24
#Solution 1
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        temp = head
        temp1 = head.next
        temp3 = temp1.next

        temp1.next = temp
        temp.next = self.swapPairs(temp3)

        return temp1
    
#Solution 2
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        temp = head.next
        head.next = self.swapPairs(temp.next)
        temp.next = head

        return temp
        
        
        