class Solution(object):
    def isAcronym(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: bool
        """
        ans=[]
        for i in words:
            ans.append(i[0])
        return s=="".join(ans)