class Solution(object):
    def percentageLetter(self, s, letter):
        """
        :type s: str
        :type letter: str
        :rtype: int
        """
        c=0
        for i in s:
            if i==letter:
                c+=1
        return int((float(c)/len(s))*100)