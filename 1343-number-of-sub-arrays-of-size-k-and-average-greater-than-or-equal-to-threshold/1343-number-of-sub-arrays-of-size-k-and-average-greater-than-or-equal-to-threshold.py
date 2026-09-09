class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        Sum=0
        count=0
        for i in range(k):
            Sum+=arr[i]
        if Sum/k>=threshold:
            count+=1
        for i in range(k,len(arr)):
            Sum+=arr[i]
            Sum-=arr[i-k]
            if Sum/k>=threshold:
                count+=1
        return count