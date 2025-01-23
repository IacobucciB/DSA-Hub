#include <iostream>
#include <algorithm>

class Solution {
public:
    bool isAnagram(string s, string t) {
        sort(s.begin(), s.end());
        sort(t.begin(), t.end());
        return s == t;
    }
};

int main() {
    string s = "rat";
    string t = "tar";
    cout << (isAnagram(s1, s2) ? "true" : "false") << endl;
    return 0;
}
