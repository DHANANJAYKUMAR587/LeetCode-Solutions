class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        total=[]
        for i in range(len(blocks)-k+1):
            ans=[]
            for j in range(i,i+k):
                ans.append(blocks[j])
            count=0
            for l in ans:
                if l=="W":
                    count+=1
            total.append(count)
        return min(total)
        