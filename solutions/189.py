class Solution:
    '''
    Prompt: 
    Given an integer array nums move all of the elements to the right k times. 

    Questions:
    Can we assume that we receive valid inputs when the function is called? 
    Will K ever be negative? So in this case we will shift elements to the left? 

    Thought process: 
    Iterate through K and create a result O(n) time | O(n) space 

    Example input: nums = [0, 1, 2, 3] k = 2 
    Thought 1: nums[i+k] = nums[i] -> out of range index errors. 
    Thought 2: i = 2 new index = i + k % len(nums)

    Optimal Solution: O(n) Time, O(1) Space: 
    Convert k to k % len(nums) to see how many times we need to move items over
    Afterwards, reverse the entire array to get closer to the shifted array we want
    Then on the first k elements reverse them 
    Reverse the last k elements
    '''
    def reverse(self, nums: List[int], left: int, right: int) -> None:
        while left < right: 
            nums[left], nums[right] = nums[right], nums[left]
            left += 1 
            right -= 1 

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n 
        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)