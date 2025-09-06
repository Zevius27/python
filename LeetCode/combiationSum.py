# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []

        def backtrack(start, curr, total):
            # If we hit the target, store the current combination
            if total == target:
                res.append(curr[:])   # make a copy
                return
            # If we go past the target, stop exploring
            if total > target:
                return

            # Explore choices
            for i in range(start, len(candidates)):
                # choose
                curr.append(candidates[i])
                # explore (same i allowed because unlimited use)
                backtrack(i, curr, total + candidates[i])
                # undo (backtrack)
                curr.pop()

        backtrack(0, [], 0)
        return res


# Example
sol = Solution()
print(sol.combinationSum([2, 3, 6, 7], 7))
