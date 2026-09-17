class Solution(object):
    def findColumnWidth(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        total=[]
        for i in range(len(grid[0])):
            ans = []
            for row in grid:
                ans.append(len(str(row[i])))
            total.append(max(ans))
        return total