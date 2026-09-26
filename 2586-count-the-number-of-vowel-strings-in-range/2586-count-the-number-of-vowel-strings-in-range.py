class Solution(object):
    def vowelStrings(self, words, left, right):
        """
        :type words: List[str]
        :type left: int
        :type right: int
        :rtype: int
        """
        count=0
        A="aeiou"
        for i in range(left,right+1):
            if words[i][0] in A and words[i][-1] in A:
                count+=1
        return count