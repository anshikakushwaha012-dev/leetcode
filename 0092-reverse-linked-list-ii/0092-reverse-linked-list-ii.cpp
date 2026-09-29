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
    ListNode* reverseBetween(ListNode* head, int left, int right) {
    ListNode*temp=head;
    vector<int>v;
    while(temp!=NULL){
        v.push_back(temp->val);
        temp=temp->next;
    }   
    temp=head;
    for(int i=1;i<left; i++){
            temp = temp->next;
        }
    for(int i=right-1;i>=left-1;i--){
        temp->val=v[i];
        temp=temp->next;
    }
    return head;
    }
};