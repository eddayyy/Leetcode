#include <limits> 

class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int n = nums.size();
        int left = 0, total = 0, subSeq = std::numeric_limits<int>::max(); 

        for (int right = 0; right <= n - 1; right++) {
            total += nums[right]; 
            while (total >= target) { 
                subSeq = std::min(subSeq, right - left + 1); 
                total -= nums[left]; 
                left += 1;   
            }
        }
        return subSeq == std::numeric_limits<int>::max() ? 0 : subSeq;
    }
};