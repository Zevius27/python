
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21
 

# Constraints:

# -231 <= x <= 231 - 1















class Solution:
    # Check if num is under 2**31 && -2**31
    def reverse(self, x: int) -> int:
        
        reversedInt = str(x)
        # reverse it 
        resultMax = 2**31   
        resultMin = -2**31
        reversedInt = reversedInt[::-1]
        if "-" in reversedInt:
            # take out - in the back
            reversedInt = reversedInt[0:reversedInt.__len__()-1]
            # add - sign And int conversion
            sign = "-"
            reversedInt = int(sign + reversedInt)
            if resultMin <= reversedInt <= resultMax:
                print(reversedInt)
                return reversedInt
            else:
                return 0
        else:
            resultMax = 2**31   
            reversedInt = int(reversedInt)
            if reversedInt <= resultMax:
                return reversedInt
            else:
                return 0
        




sol1 = Solution()
sol1.reverse(-123)