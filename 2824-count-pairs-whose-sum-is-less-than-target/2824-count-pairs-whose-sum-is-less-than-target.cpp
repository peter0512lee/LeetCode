class Solution {
public:
    int countPairs(vector<int>& nums, int target) {
        // sort the nums
        ranges::sort(nums);
        
        // init two pointer, head and tail
        int n = nums.size();
        int left = 0, right = n - 1, ans = 0;
        
        // main algo
        while (left < right) {
            if (right > n) continue;
            int sum = nums[left] + nums[right];
            if (sum < target) {
                ans += right - left;
                left++;
            } else {
                right--;
            }
        }

        return ans;
    }
};