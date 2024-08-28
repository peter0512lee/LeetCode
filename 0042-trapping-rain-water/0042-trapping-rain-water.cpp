class Solution {
public:
    int trap(vector<int>& height) {
        // T: O(n)
        // S; O(1)
        int left = 0;
        int right = height.size() - 1;
        int pre_max = 0;
        int suf_max = 0;
        int ans = 0;

        while (left <= right) {
            pre_max = max(pre_max, height[left]);
            suf_max = max(suf_max, height[right]);

            if (pre_max < suf_max) {
                ans += pre_max - height[left];
                left++;
            } else {
                ans += suf_max - height[right];
                right--;
            }
        }

        return ans;
    }
};