class Solution(object):
    def calculateScore(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        a=bin(a)[2:]
        b=bin(b)[2:]
        s1=0
        s2=0
        for i in a:
            if i=="1":
                s1+=1
        for i in b:
            if i=="1":
                s2+=1
        if s1>=s2:
            return s1*s2
        else:
            return s2/s1
        