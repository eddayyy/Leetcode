#include <vector>
#include <unordered_map>

class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& numbers, int target) {
        if (numbers.size() <= 1) {
            return {};
         }
        int left = 0, right = numbers.size() - 1; 
        while (left < right) {
            int sum = numbers[left] + numbers[right];
            if (sum > target) { right--; }
            else if (sum < target) { left++; }
            else { return {left + 1, right + 1}; } 
        }
        return {};
    }
};