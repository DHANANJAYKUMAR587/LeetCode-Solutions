class Solution(object):
    def findChampion(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans=[]
        for i in grid:
            ans.append(sum(i))
        return ans.index(max(ans))