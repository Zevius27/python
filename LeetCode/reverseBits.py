# Reverse bits of a given 32 bits signed integer.

 

# Example 1:

# Input: n = 43261596

# Output: 964176192

# Explanation:

# Integer	Binary
# 43261596	00000010100101000001111010011100
# 964176192	00111001011110000010100101000000
# Example 2:

# Input: n = 2147483644

# Output: 1073741822

# Explanation:

# Integer	Binary
# 2147483644	01111111111111111111111111111100
# 1073741822	00111111111111111111111111111110
 

# Constraints:

# 0 <= n <= 231 - 2
# n is even.
 

# Follow up: If this function is called many times, how would you optimize it?





class Solution:
    def reverseBits(self, n: int) -> int:
        binNum = str(bin(n))
        binNum = binNum[2:]
        if len(binNum) <= 32:
            binNum = "0" * (32 - len(binNum)) + binNum
        binNum = binNum[::-1]
        print(int(binNum,2))
        return int(binNum,2)
        


sol = Solution()
sol.reverseBits(43261596)
















