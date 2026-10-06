class Solution {
public:
    void reorderList(ListNode* head) {
        ListNode*slow=head;
        ListNode*fast=head;

        while(fast!=NULL && fast->next!=NULL){
            slow=slow->next;
            fast=fast->next->next;
        }

        ListNode*cur=slow->next;
        slow->next=NULL;

        ListNode*prev=NULL;
        while(cur!=NULL){
            ListNode*next=cur->next;
            cur->next=prev;
            prev=cur;
            cur=next;
        }

        ListNode*p1=head;
        ListNode*p2=prev;

        while(p2!=NULL){
            ListNode*next1=p1->next;
            ListNode*next2=p2->next;

            p1->next=p2;
            p2->next=next1;

            p1=next1;
            p2=next2;
        }
    }
};