class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        ranges::sort(nums);
        vector<vector<int>> ans;
        int n = nums.size();
        for (int a = 0; a < n - 3; a++) {
            long long x = nums[a];
            if (a > 0 && x == nums[a - 1]) continue;
            for (int b = a + 1; b < n - 2; b++) {
                long long y = nums[b];
                if (b > a + 1 && y == nums[b - 1]) continue;
                int c = b + 1;
                int d = n - 1;
                while (c < d) {
                    long long s = x + y + nums[c] + nums[d];
                    if (s > target) {
                        d--;
                    } else if (s < target) {
                        c++;
                    } else {
                        ans.push_back({(int) x, (int) y, nums[c], nums[d]});
                        for (c++; c < d && nums[c] == nums[c - 1]; c++);
                        for (d--; d > c && nums[d] == nums[d + 1]; d--);
                    }
                }
            }
        }
        return ans;
    }
};