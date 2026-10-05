/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    bool isPalindrome(ListNode* head) {
        ListNode*slow=head;
        ListNode*fast=head;
        while(fast!=NULL && fast->next!=NULL){
            slow=slow->next;
            fast=fast->next->next;
        }
        ListNode*cur=slow;
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
            if(p1->val!=p2->val){
                return false;
            }
            p1=p1->next;
            p2=p2->next;
        }
        return true;
    }
};