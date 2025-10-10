# Given two strings s and t, return true if t is an anagram of s, and false otherwise.


# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false



class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        for i in s:
            if i in t:
                t = t.replace(i,"",1)
        if len(t) == 0:
            return True
        else:
            return False
            
s = Solution()
s.isAnagram("anagram","nagaram")