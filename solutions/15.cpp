#include <vector> 

class Solution {
public:
    std::vector<std::vector<int>> threeSum(std::vector<int>& nums) {
        std::vector<std::vector<int>> result; 
        std::sort(nums.begin(), nums.end()); 
        int n = nums.size(); 

        for ( int i = 0; i < n - 2; i++ ) {
            if ( i > 0 && nums[i] == nums[i - 1] ) continue;
            
            int left = i + 1;
            int right = n - 1; 

            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right]; 
                if ( sum == 0 ) {
                    result.push_back({nums[i], nums[left], nums[right]});

                    // Skip duplicates for the left pointer
                    while ( left < right && nums[left] == nums[left + 1] ) left++; 

                    // Skip duplicates for the right pointer
                    while ( left < right && nums[right] == nums[right - 1] ) right--; 

                    ++left;
                    --right;
                } else if ( sum < 0) {
                    ++left; 
                } else {
                    --right; 
                }
            }
        }

        return result;
    }
};