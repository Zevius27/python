# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

 
class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        res = nums1 & nums2 
        result = []
        for i in res:
            result.append(i)
        return result