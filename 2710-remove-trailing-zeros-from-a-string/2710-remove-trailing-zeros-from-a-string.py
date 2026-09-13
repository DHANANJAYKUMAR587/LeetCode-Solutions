class Solution(object):
    def removeTrailingZeros(self, num):
        """
        :type num: str
        :rtype: str
        """
        a=int(num)
        while a%10==0:
            a=a//10
        return str(a)