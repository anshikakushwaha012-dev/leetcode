# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev=head
        curr=head.next
        position=1
        first=-1
        last=-1
        min_distance=float('inf')
        while curr.next:
            next_node=curr.next
            if ((curr.val>prev.val and curr.val>next_node.val) or
                (curr.val < prev.val and curr.val<next_node.val)):
                if first==-1:
                    first=position
                else:
                    min_distance=min(min_distance,position-last)
                last=position
            prev=curr
            curr=curr.next
            position+=1
        if first==-1 or first==last:
            return [-1,-1]
        max_distance=last-first
        return [min_distance,max_distance]