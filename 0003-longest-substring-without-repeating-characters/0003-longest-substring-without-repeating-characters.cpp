class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int n = s.length(), ans = 0, left = 0;
        unordered_set<char> window; // matain the char from left and right
        for (int right = 0; right < n; right++) {
            char c = s[right];
            while (window.count(c)) {
                window.erase(s[left++]);
            }
            window.insert(c);
            ans = max(ans, right - left + 1);
        }
        return ans;
    }
};