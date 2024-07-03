/**
 * Your TwoSum object will be instantiated and called as such:
 * TwoSum* obj = new TwoSum();
 * obj->add(number);
 * bool param_2 = obj->find(value);
 */
#include <unordered_map>
#include <limits>

class TwoSum {
private:
    std::unordered_map<int, int> num_count; 

public:
    TwoSum() {
        num_count.clear(); 
    }
    
    void add(int number) {
        num_count[number]++; 
    }
    
    bool find(int value) {
        for (const auto& entry : num_count) {
            int num1 = entry.first;
            long num2 = long(value) - long(num1);
            // Check if num2 is in the map and ensure that if num1 == num2, there are at least two occurrences
            if ((num1 == num2 && entry.second > 1) || (num1 != num2 && num_count.count(num2))) {
                return true;
            }
        }
        return false;
    }
};
