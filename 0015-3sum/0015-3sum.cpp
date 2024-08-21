class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        ranges::sort(nums);
        vector<vector<int>> ans;
        int n = nums.size();
        for (int i = 0; i < n - 2; i++) {
            int x = nums[i];
            if (i && x == nums[i - 1]) continue;
            if (x + nums[i + 1] + nums[i + 2] > 0) break; // optimize 1
            if (x + nums[n - 2] + nums[n - 1] < 0) continue; // optimize 2
            int j = i + 1, k = n - 1;
            while (j < k) {
                int sum = x + nums[j] + nums[k];
                if (sum > 0) {
                    k--;
                } else if (sum < 0) {
                    j++;
                } else {
                    ans.push_back({x, nums[j], nums[k]});
                    for (j++; j < k && nums[j] == nums[j - 1]; j++);
                    for (k--; k > j && nums[k] == nums[k + 1]; k--);
                }
            }
        }
        return ans;
    }
};