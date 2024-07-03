# Merge Sort implementation
class Solution:
    def merge(self, nums, L, M, R):
        left, right = nums[L:M+1], nums[M+1:R+1]
        
        i, j, k = L, 0, 0

        arrLSize, arrRSize = len(left), len(right) 
        while j < arrLSize and k < arrRSize:
            if left[j] <= right[k]:
                nums[i] = left[j]
                j += 1
            else:
                nums[i] = right[k] 
                k += 1
            i += 1
        while j < arrLSize:
            nums[i] = left[j] 
            j += 1 
            i += 1 
        while k < arrRSize:
            nums[i] = right[k]
            i += 1
            k += 1 

    def mergeSort(self, nums, l, r):
        if l == r:
            return nums
        
        m = (l + r) // 2 
        self.mergeSort(nums, l, m) 
        self.mergeSort(nums, m + 1, r) 

        self.merge(nums, l, m, r)

        return nums

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums, 0, len(nums) - 1 )    