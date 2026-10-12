class Solution(object):
    def oddString(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        A="abcdefghijklmnopqrstuvwxyz"
        total=[]
        for i in words:
            ans=[]
            for j in i:
                ans.append(A.index(j))
            b=[]
            for i in range(len(ans)-1):
                b.append(ans[i+1]-ans[i])
            total.append(b)
        from collections import Counter
        freq=Counter(tuple(x) for x in total)
        for i in range(len(total)):
            if freq[tuple(total[i])]==1:
                return words[i]