#include <iostream>
#include <unordered_map>

class Solution {
public:
    int romanToInt(std::string s) {
        std::unordered_map<char, int> roman = {
            {'I', 1}, {'V', 5}, {'X', 10}, {'L', 50},
            {'C', 100}, {'D', 500}, {'M', 1000}
        };
        int result = 0;
        int prev_value = 0;
        for (size_t i = 0; i < s.length(); ++i) {
            char c = s[i];
            int value = roman[c];
            if (value > prev_value) {
                result += value - 2 * prev_value;
            } else {
                result += value;
            }
            prev_value = value;
        }
        return result;
    }
};

int main() {
    Solution solution;
    std::cout << solution.romanToInt("MCMXCIV") << std::endl;
    return 0;
}