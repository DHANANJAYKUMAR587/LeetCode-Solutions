# LeetCode 4038 - Sum of Decoded Numbers
# Difficulty: Easy
#
# Problem:
# Each number in nums is encoded using a width value in its
# last digit. The remaining digits are split into x and y
# using that width.
#
# The decoded value is x^y.
# Return the sum of all decoded values modulo 10^9 + 7.
#
# Example:
# nums = [2522, 2101]
# Output = 1649
#
# Approach:
# 1. Get width from the last digit.
# 2. Remove the last digit to get d.
# 3. Split d into x and y using width.
# 4. Calculate x^y using modular exponentiation.
# 5. Add the result to the answer.
class Solution(object):
    def sumDecoded(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total=0
        MOD=10**9+7
        for i in range(len(nums)):
            wid=nums[i]%10
            nums[i]=nums[i]//10
            x=int(str(nums[i])[:wid])
            y=int(str(nums[i])[wid:])
            total=(total+pow(x,y,MOD))%MOD
        return total