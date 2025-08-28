# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


# Example 1:

# Input: nums = [1,2,3,1]

# Output: true

# Explanation:

# The element 1 occurs at the indices 0 and 3.

# Example 2:

# Input: nums = [1,2,3,4]

# Output: false

# Explanation:

# All elements are distinct.

# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]

# Output: true


# Constraints:

# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109



# class Solution:
#     def containsDuplicate(self, nums) -> bool:
#         if nums.__len__() <= 1:
#                 print("False")
#                 return False  
#         ele = nums.pop()

#         for i in range(0,nums.__len__()):
#             if ele in nums:
#                 print("True")
#                 return True
#             if nums.__len__() <= 1:
#                 print("False")
#                 return False
#             ele = nums.pop()
       
    





num = [1,2,3,1]

# Try 2
# using set

class Solution:
    def containsDuplicate(self, nums) -> bool:
        num2 = set(nums)
        if num2.__len__() < nums.__len__():
            return True
        else:
            return False




    
sol = Solution()
sol.containsDuplicate(num)