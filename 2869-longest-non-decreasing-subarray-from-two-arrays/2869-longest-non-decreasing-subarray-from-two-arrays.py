class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:

        @cache
        def dp(i, prev):
            if i == len(nums1):
                return 0
            

            res = 0

            if not prev:
                res = dp(i + 1, prev)
            
            if prev <= nums1[i]:
                res = max(res, 1 + dp(i + 1, nums1[i]))
            if prev <= nums2[i]:
                res = max(res, 1 + dp(i + 1, nums2[i]))

            return res
        
        return dp(0, 0)


f=open('user.out','w')
nums_arr = []
solve = Solution()
for nums in map(loads,stdin): 
    if len(nums_arr) < 2:
        nums_arr.append(nums)
    else:
        print(solve.maxNonDecreasingLength(nums_arr.pop(0), nums_arr.pop(0)),file=f)
        nums_arr.append(nums)
print(solve.maxNonDecreasingLength(nums_arr.pop(0), nums_arr.pop(0)),file=f)



        