# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1=0
        place=1
        while l1:
            num1+=l1.val*place
            l1=l1.next
            place*=10
        num2=0
        place=1
        while l2:
            num1+=l2.val*place
            l2=l2.next
            place*=10
        



        total=num1+num2
        if total==0:
            return ListNode(0)
        dummy=ListNode(0)
        tail=dummy
        while total:
            tail.next=ListNode(total%10)
            tail=tail.next
            total//=10
        return dummy.next    


                
        