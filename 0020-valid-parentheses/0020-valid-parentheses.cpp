class Solution {
public:
    bool isValid(string s) {
        vector<char> stack;
        unordered_map<char, char> pairs = {
            {'(', ')'},
            {'{', '}'},
            {'[', ']'}
        };
        for (char i : s) {
            if (i == '(' || i == '{' || i == '[') {
                stack.push_back(i);
            }
            else {
                if (stack.empty()) {
                    return false;
                }
                char top = stack.back();
                stack.pop_back();
                if (pairs[top] != i) {
                    return false;
                }
            }
        }
        return stack.empty();
    }
};