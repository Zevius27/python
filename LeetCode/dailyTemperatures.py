# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.


# Example 1:

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
# Example 2:

# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
# Example 3:

# Input: temperatures = [30,60,90]
# Output: [1,1,0]


# Constraints:

# 1 <= temperatures.length <= 105
# 30 <= temperatures[i] <= 100

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []  # stores indices of unresolved (cooler) days

        for i, temp in enumerate(temperatures):
            # check if current temp is warmer than last stacked day's temp
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_day = stack.pop()
                result[prev_day] = i - prev_day  # days waited
            stack.append(i)
        return result


# Example tests
s = Solution()
print(s.dailyTemperatures([73,74,75,71,69,72,76,73]))  # [1,1,4,2,1,1,0,0]
print(s.dailyTemperatures([30,40,50,60]))              # [1,1,1,0]
print(s.dailyTemperatures([30,60,90]))                 # [1,1,0]

s = Solution()
# s.dailyTemperatures([30,60,90]) #[1,1,0]
# s.dailyTemperatures([30,40,50,60])
# [3,1,1,2,1,1,0,1,1,0]
# s.dailyTemperatures([55, 38, 53, 81, 61, 93, 97, 32, 43, 78])
