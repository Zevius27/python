# Given a 32-bit integer num, return a string representing its hexadecimal representation. For negative integers, two’s complement method is used.

# All the letters in the answer string should be lowercase characters, and there should not be any leading zeros in the answer except for the zero itself.

# Note: You are not allowed to use any built-in library method to directly solve this problem.

 

# Example 1:

# Input: num = 26
# Output: "1a"
# Example 2:

# Input: num = -1
# Output: "ffffffff"




class Solution:
    def toHex(self, num: int) -> str:
        if str(num)[0] != "-":
            res = str(hex(num))[2:]
            return res
        else:
            num = abs(num)
            binNum = bin(num)
            if len(str(binNum)) != 32:
                binNum = str(binNum)[2:]
                binNum = "0" * (32 - len(binNum)) + binNum
            revBinNum = ""
            for i in binNum:
                if i == "0":
                    revBinNum = revBinNum + "1"
                else:
                    revBinNum = revBinNum + "0"
            intRes = int(revBinNum,2)
            intRes = intRes + 1
            res =  str(hex(intRes))[2:]
            return res

s = Solution()
s.toHex(-1)