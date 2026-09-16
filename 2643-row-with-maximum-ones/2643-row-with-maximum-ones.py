class Solution(object):
    def rowAndMaximumOnes(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        ans=[]
        for i in range(len(mat)):
            a=mat[i].count(1)
            ans.append(a)
        Max=ans[0]
        for i in ans:
            if i>Max:
                Max=i
        return ans.index(Max),Max