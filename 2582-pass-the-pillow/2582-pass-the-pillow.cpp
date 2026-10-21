class Solution {
public:
    int passThePillow(int n, int time) {
        int t = time % (2 * (n - 1));
        return t < n ? t + 1 : 2 * n - 1 - t;
    }
};