class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen=set()
        count=1
        for i in s:
            if i in seen:
                count+=1
                seen.clear()
            seen.add(i)
        return count