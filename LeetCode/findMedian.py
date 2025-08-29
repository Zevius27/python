

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # edge = [] , [0] , [0]  []
        if nums1.__len__() == 0 and nums2.__len__() <= 1:
            return nums2
        if nums2.__len__() == 0 and nums1.__len__() <= 1:
            return nums1
        # edge 2 = [] , [1,2,3,4]
        nums3 = nums1 + nums2
        if nums3.__len__() % 2 == 0:
            print(nums3)
            rs1 = nums3[nums3.__len__()//2-1]
            rs2 = nums3[nums3.__len__()//2]
            result = (rs1 + rs2)/2
            return result
        else:
            return nums3[nums3.__len__()//2+1]


sol = Solution()
sol.findMedianSortedArrays([1, 2], [3, 4])
