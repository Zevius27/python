







# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.











num = [3, 0, 1]


class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = nums.__len__()
        if n <= 1:
            return
        nums2 = []
        
        for i in range(min(num),n + 1):
            nums2.append(i) 
        set1 = set(nums)
        set2 = set(nums2)
        res = set1 ^ set2
        for i in res:
            i = str(i)
            res = int(i)
        print(res)
        return res

sol = Solution()
sol.missingNumber(num)