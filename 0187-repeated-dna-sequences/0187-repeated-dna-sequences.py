class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        seen=set()
        result=set()
        for i in range(len(s)-9):
            a=s[i:i+10]
            if a in seen:
                result.add(a)
            else:
                seen.add(a)
        return list(result)