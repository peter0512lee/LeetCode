class Solution {
public:
    int getLucky(string s, int k) {
        string int_s = "";
        for (auto c : s) {
            int int_c = c - 'a' + 1;
            int_s += to_string(int_c);
        }

        for (int i = 0; i < k; i++) {
            int sum = 0;
            for (auto c : int_s) {
                sum += c - '0';
            }
            int_s = to_string(sum);
        }

        return stoi(int_s);
    }
};