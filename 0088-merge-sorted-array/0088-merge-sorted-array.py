class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = m + n - 1
        i = m - 1
        j = n - 1

        while i >= 0 or j >= 0:
            if i >= 0 and j >= 0 and nums1[i] > nums2[j]:
                nums1[last] = nums1[i]
                i -= 1
            elif i >= 0 and j >= 0 and nums1[i] <= nums2[j]:
                nums1[last] = nums2[j]
                j -= 1
            elif i >= 0:
                nums1[last] = nums1[i]
                i -= 1
            else:
                nums1[last] = nums2[j]
                j -= 1  
            last -= 1
        return nums1