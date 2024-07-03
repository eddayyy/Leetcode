#include <vector>           // Dynamic Array C++ STL Container
class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        /*
        Time (n) | Space O(1) 
        */
        std::vector<int> charCount(26, 0); 

        for ( char c : magazine ) {
            charCount[c - 'a']++; 
        }

        for (char c : ransomNote ) { 
            if ( charCount[c - 'a'] == 0 ) return false; 

            charCount[c -'a']--; 
        }
        return true; 
    }
};