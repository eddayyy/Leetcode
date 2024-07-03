class Solution {
public:
    bool isSubsequence(string s, string t) {
        int sLen = s.length();
        int tLen = t.length(); 
        int i = 0, j = 0; 
        while ( i < sLen && j < tLen) {
            if (s[i] == t[j]) {
                i++; 
            }
            j++;
        }
        return i == sLen; 
    }
};