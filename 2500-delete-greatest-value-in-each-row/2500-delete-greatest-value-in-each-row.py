class Solution(object):
    def deleteGreatestValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans=[]
        while len(grid[0])>0:
            maximum=0
            for i in grid:
                mx=max(i)
                maximum=max(mx,maximum)
                i.remove(mx)
            ans.append(maximum)
        return sum(ans)
