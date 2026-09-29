# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        temp=head
        v=[]
        while temp!=None:
            v.append(temp.val)
            temp=temp.next
        temp=head
        for i in range(len(v)- 1,-1,-1):
            temp.val=v[i]
            temp=temp.next
        return head