class Solution(object):
    def kItemsWithMaximumSum(self, numOnes, numZeros, numNegOnes, k):
        """
        :type numOnes: int
        :type numZeros: int
        :type numNegOnes: int
        :type k: int
        :rtype: int
        """
        ans=[]
        for i in range(numOnes):
            ans.append(1)
        for i in range(numZeros):
            ans.append(0)
        for i in range(numNegOnes):
            ans.append(-1)
        import heapq
        heap=[]
        for i in ans:
            heapq.heappush(heap,i)
        return sum(heapq.nlargest(k,heap))