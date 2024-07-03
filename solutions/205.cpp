#include <unordered_map> 

class Solution {
public:
    bool isIsomorphic(string s, string t) {
        if ( s.length() != t.length() ) return false; 
        std::unordered_map<char, char> sMap, tMap; 
        // Example input: s = "foo" t = "bar"
        // f -> b
        // b -> f
        // o -> a 
        // a -> o 
        for (int i = 0; i < s.length(); ++i) {
            // Check now if they are already in the hashmap and map to different chars 
            if ( (tMap.count(t[i]) && tMap[t[i]] != s[i]) || 
                 (sMap.count(s[i]) && sMap[s[i]] != t[i]) ) return false; 
            sMap[s[i]] = t[i]; // e -> a
            tMap[t[i]] = s[i]; // a -> e 
        }
        return true;
    }
};