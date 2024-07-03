class Solution {
public:
    int maxArea(vector<int>& height) {
        int n = height.size(); 
        if (n <= 1) { return 0; }

        int left = 0, right = n - 1, maxArea = 0;
        while (left < right) { 
            int area = (right - left) * std::min(height[left], height[right]); // Area = Width * Min. Height
            maxArea = std::max(maxArea, area);
            if (height[left] < height[right]) { left++; }
            else if (height[left] > height[right]) { right--; }
            else { right --; }
        }

        return maxArea;
    }
};