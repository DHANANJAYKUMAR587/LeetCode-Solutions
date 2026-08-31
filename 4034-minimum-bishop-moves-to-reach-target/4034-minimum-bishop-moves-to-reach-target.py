class Solution(object):
    def minBishopMoves(self, source, target):
        """
        :type source: List[int]
        :type target: List[int]
        :rtype: int
        """
        ans=[]
        if source[0]%2==0:
            if source[1]%2!=0:
                ans.append("Black")
            else:
                ans.append("white")
        elif source[0]%2!=0:
            if source[1]%2==0:
                ans.append("Black")
            else:
                ans.append("white")
        if target[0]%2==0:
            if target[1]%2!=0:
                ans.append("Black")
            else:
                ans.append("white")
        elif target[0]%2!=0:
            if target[1]%2==0:
                ans.append("Black")
            else:
                ans.append("white")
        if ans[0]!=ans[1]:
            return -1
        if source == target: 
            return 0 
        if abs(source[0] - target[0]) == abs(source[1] - target[1]): 
            return 1 
        return 2