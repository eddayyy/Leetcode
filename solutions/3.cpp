class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        std::unordered_map<char, int> hashmap; 
        int left = 0, longest = 0; 

        for (int right = 0; right < s.length(); right++) {
            if (hashmap.count(s[right]) && hashmap[s[right]] >= left) { /* Check if s[right] is a duplicate */
                left = hashmap[s[right]] + 1;
            }
            hashmap[s[right]] = right; 
            longest = std::max(longest, right - left + 1); 
        }
        return longest;
    }
};