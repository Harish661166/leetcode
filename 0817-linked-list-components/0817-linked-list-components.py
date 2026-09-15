# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        num=set(nums)
        result =0
        while head:
            if head.val in num and (head.next == None or head.next.val not in num):
                result += 1
            head = head.next
        return result