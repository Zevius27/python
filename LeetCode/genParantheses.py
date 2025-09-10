

# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        resList = []

        def backtrack(current, openBracket, closingBracket):
            # Base condition: no brackets left
            if openBracket == 0 and closingBracket == 0:
                resList.append("".join(current))
                return

            # If we can still place an open bracket
            if openBracket > 0:
                current.append("(")
                backtrack(current, openBracket - 1, closingBracket)
                current.pop()  # backtrack step

            # If we can place a closing bracket
            if closingBracket > openBracket:
                current.append(")")
                backtrack(current, openBracket, closingBracket - 1)
                current.pop()  # backtrack step

        backtrack([], n, n)
        return resList


# Example
sol = Solution()
print(sol.generateParenthesis(4))
