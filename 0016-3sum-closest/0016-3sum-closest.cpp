class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        ranges::sort(nums);
        int ans, n = nums.size();
        int min_diff = INT_MAX;
        for (int i = 0; i < n - 2; i++) {
            int j = i + 1;
            int k = n - 1;
            while (j < k) {
                int sum = nums[i] + nums[j] + nums[k];
                
                if (sum == target) {
                    return target;
                } else if (sum > target) {
                    if (sum - target < min_diff) {
                        min_diff = sum - target;
                        ans = sum;
                    }
                    k--;
                } else {
                    if (target - sum < min_diff) {
                        min_diff = target - sum;
                        ans = sum;
                    }
                    j++;
                }
            }
        }
        return ans;
    }
};