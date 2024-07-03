class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        list1, list2 = [], []

        for num in nums1:
            if num not in nums2 and num not in list1: 
                list1.append(num)
        for num in nums2: 
            if num not in nums1 and num not in list2:
                list2.append(num) 
                
        return [list1, list2]