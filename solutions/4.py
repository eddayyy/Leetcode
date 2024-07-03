class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2): return self.findMedianSortedArrays(nums2, nums1)

        A, B = nums1, nums2 
        total = len(A) + len(B)
        half = total // 2
        
        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2 # A's Pointer
            j = half - i - 2 # B's Pointer
            
            Aleft = A[i] if i >= 0 else float('-inf')
            Aright = A[i + 1] if (i + 1) < len(A) else float('inf')

            Bleft = B[j] if j >= 0 else float('-inf')
            Bright = B[j + 1] if (j + 1) < len(B) else float('inf')

            if Aleft <= Bright and Bleft <= Aright:
                # odd case
                if total % 2 == 1:
                    return min(Aright, Bright)
                # even case
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright: 
                r = i - 1
            else:
                l =  i + 1

        return 0 