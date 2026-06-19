# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        l = 0 

        curr = head

        while curr:

            l +=1
            curr = curr.next

        distance =  l - n

        if distance == 0:
            return head.next

        curr = head

        i = 0

        while i < distance:

            i +=1

            if i == distance:
                curr.next = curr.next.next
                break
            else:
                curr = curr.next
        return head