class Solution(object):
    def checkDistances(self, s, distance):
        """
        :type s: str
        :type distance: List[int]
        :rtype: bool
        """
        isSame=True
        a=list(set(s))
        for i in a:
            an=[]
            for idx,val in enumerate(s):
                if i==val:
                    an.append(idx)
            c=an[1]-an[0]-1
            if (distance[ord(i)-ord("a")])!=c:
                isSame=False
                break
        return isSame