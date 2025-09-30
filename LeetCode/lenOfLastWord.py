# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal substring consisting of non-space characters only.

 

# Example 1:

# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
# Example 2:

# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
# Example 3:

# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.
 

# Constraints:

# 1 <= s.length <= 104
# s consists of only English letters and spaces ' '.
# There will be at least one word in s.
 




class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 1 and s[0] != " ":
            return 1
        if len(s) ==  1 and s[0] == " ":
            return 0

        wordLen = 0
        for i in range(len(s),0,-1):
            if s[-1] == " ":
                s = s[0:-1]
            else:
                break
        for i in range(len(s)-1,-1,-1):
            if s[i] != " ":
                wordLen += 1
            else:
                break
        return wordLen
    
        


s = Solution()
s.lengthOfLastWord("a  ")