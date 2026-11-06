class Solution(object):
    def equalFrequency(self, word):
        """
        :type word: str
        :rtype: bool
        """
        d={}
        for i in word:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        a=sorted(d.values())
        if len(set(a))==1:
            if a[0]==1 or len(a)==1:
                return True
            return False
        if a[0]==1 and len(set(a[1:]))==1:
            return True
        if a[-1]-a[-2]==1 and len(set(a[:-1]))==1:
            return True
        return False