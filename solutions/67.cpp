#include <string> 
#include <algorithm> 

class Solution { 

public: 
    std::string addBinary(std::string a, std::string b) { 
        int i = a.length() - 1; 
        int j = b.length() - 1;
        int carry = 0; 
        std::string result; 

        while (i >= 0 || j >= 0 || carry) { 
            int total = carry; 
            if (i >= 0){
                total += a[i] - '0';
                i--;
            }
            if (j>= 0) {
                total += b[j] - '0';
                j--; 
            }
            carry = total / 2; 
            result.push_back(total % 2 + '0');    
        }
        std::reverse(result.begin(), result.end()); 
        return result;
    }
};