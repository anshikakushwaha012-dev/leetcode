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
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode*dummy=new ListNode(0);
        dummy->next=head;
        ListNode*prev=dummy;
        ListNode*ptr=head;
        while (ptr!=NULL){
            if (ptr->next!=NULL && ptr->val==ptr->next->val){
                int value=ptr->val;
                while (ptr!=NULL && ptr->val==value){
                    ptr=ptr->next;
                }
                prev->next=ptr;
            }
            else{
                prev=ptr;
                ptr=ptr->next;
            }
        }
        return dummy->next;
    }
};