class Solution {
public:
    void reorderList(ListNode* head) {
        vector<int> arr;
        ListNode* cur = head;
        while (cur != NULL) {
            arr.push_back(cur->val);
            cur = cur->next;
        }
        int left=0;
        int right= arr.size() - 1;
        cur = head;
        while (left <= right) {
            if (left ==  right) {
                cur->val = arr[left];
                break;
            }
            cur->val = arr[left];
            cur = cur->next;
            cur->val = arr[right];
            cur = cur->next;
            left++;
            right--;
        }
    }
};