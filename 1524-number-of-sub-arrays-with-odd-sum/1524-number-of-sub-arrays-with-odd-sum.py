class Solution(object):
    def numOfSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # ans=[]
        # for i in range(len(arr)):
        #     for j in range(i,len(arr)):
        #         ans.append(sum(arr[i:j+1]))
        # count=0
        # for i in ans:
        #     if i%2!=0:
        #         count+=1
        # return count
        o=0
        e=1
        s=0
        count=0
        for i in arr:
            s+=i
            if s%2!=0:
                count+=e
                o+=1
            else:
                count+=o
                e+=1
        return count%(10**9+7)

