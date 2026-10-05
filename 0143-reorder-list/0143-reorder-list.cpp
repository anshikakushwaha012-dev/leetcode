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
    void reorderList(ListNode* head) {
        vector<ListNode*>arr;
        ListNode*cur=head;
        while(cur!=NULL){
            arr.push_back(cur);
            cur=cur->next;
        }
        int left=0;
        int right=arr.size()-1;
        while(left<right){
            arr[left]->next=arr[right];
            left++;
            if(left==right){
                break;
            }
            arr[right]->next=arr[left];
            right--;
        }
        arr[left]->next=NULL;
    }
};