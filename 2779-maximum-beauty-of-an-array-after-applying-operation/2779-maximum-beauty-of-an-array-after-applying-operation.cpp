class Solution {
public:
    int maximumBeauty(vector<int>& nums, int k) {
        // https://leetcode.cn/problems/maximum-beauty-of-an-array-after-applying-operation/solutions/2345805/pai-xu-shuang-zhi-zhen-by-endlesscheng-hbqx/
        ranges::sort(nums);
        int ans = 0, left = 0;
        for (int right = 0; right < nums.size(); right++) {
            while (nums[right] - nums[left] > k * 2) {
                left++;
            }
            ans = max(ans, right - left + 1);
        }
        return ans;
    }
};