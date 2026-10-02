class Solution(object):
    def maxScore(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        import heapq
        heap=[]
        arr = sorted(zip(nums2, nums1), reverse=True)
        total=0
        ans=0
        for n2,n1 in arr:
            heapq.heappush(heap,n1)
            total+=n1
            if len(heap)>k:
                total-=heapq.heappop(heap)
            if len(heap)==k:
                ans=max(ans,total*n2)
        return ans