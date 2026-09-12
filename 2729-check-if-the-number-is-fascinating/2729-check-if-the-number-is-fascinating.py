class Solution(object):
    def isFascinating(self, n):
        """
        :type n: int
        :rtype: bool
        """
        n1=n*2
        n2=n*3
        s=str(n)+str(n1)+str(n2)
        return len(s) == 9 and set(s) == set("123456789")