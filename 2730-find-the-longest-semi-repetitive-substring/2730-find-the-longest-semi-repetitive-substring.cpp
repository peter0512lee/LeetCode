class Solution {
public:
    int longestSemiRepetitiveSubstring(string s) {
        int ans = 1, n = s.length(), left = 0, same = 0;
        for (int right = 1; right < n; right++) {
            if (s[right] == s[right - 1]) {
                same++;
            }
            if (same > 1) {
                left++;
                while (s[left] != s[left - 1]) {
                    left++;
                }
                same--;
            }
            ans = max(ans, right - left + 1);
        }
        return ans;
    }
};