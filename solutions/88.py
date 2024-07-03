class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = m + n - 1
        '''
        Example input: 
        nums1 = [1, 2, 4, 0, 0]
        nums2 = [3, 5]

        iteration 1:
        m = 2, n = 1, last = 4 
        if 4 > 5: false => nums = [1, 2, 4, 0, 5]
        n = 0, last = 5 
        iteration 2: 
        m = 2, n = 0, last = 3
        if 4 > 3: true => nums = [1, 2, 4, 4, 5]
        m = 1, last = 2
        itertion 3: 
        m = 1, n = 0, last = 2
        if 2 > 3: false => nums = [1, 2, 3, 4, 5]
        n = -1, last = 1

        END ITERATION. 
        
        '''
        while m > 0 and n > 0: 
            if nums1[m-1] > nums2[n-1]:
                nums1[last] = nums1[m-1] 
                m -= 1 
            else: 
                nums1[last] = nums2[n-1] 
                n -= 1
            last -= 1
        
        while n > 0: 
            nums1[last] = nums2[n-1]
            n, last = n - 1, last - 1 