class Solution {
public:
    int triangleNumber(vector<int>& nums) {
        ranges::sort(nums);
        int ans = 0;

        for (int k = 2; k < nums.size(); k++) {
            int c = nums[k];
            int i = 0; // a = nums[i]
            int j = k - 1; // b = nums[j]
            while (i < j) {
                if (nums[i] + nums[j] > c) {
                    ans += j - i;
                    j--;
                } else {
                    i++;
                }
            }
        }
        return ans;
    }
};