// Title: Flatten 2D Vector
// Category: Array  
// Difficulty: Medium
class Vector2D {
public:
    Vector2D(vector<vector<int>>& vec) : nums(vec), outerPtr(0), innerPtr(0) {
        moveToNextValid(); 
    }

    int next() {
        int res = nums[outerPtr][innerPtr];
        innerPtr++; 
        moveToNextValid(); 
        return res;
    }

    bool hasNext() { 
        return outerPtr < nums.size(); 
    }

private:
    std::vector<std::vector<int>> nums;
    size_t outerPtr, innerPtr;
    void moveToNextValid() {
        while (outerPtr < nums.size() && innerPtr == nums[outerPtr].size()) {
            outerPtr++;
            innerPtr = 0;
        }
    }
};

/**
 * Your Vector2D object will be instantiated and called as such:
 * Vector2D* obj = new Vector2D(vec);
 * int param_1 = obj->next();
 * bool param_2 = obj->hasNext();
 */