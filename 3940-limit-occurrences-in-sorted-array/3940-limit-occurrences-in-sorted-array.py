class Solution(object):
    def limitOccurrences(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        ans=[]
        for key,val in d.items():
            if val>k:
                ans.append(key)
        result=[]
        for i in nums:
            if i in ans:
                continue
            else:
                result.append(i)
        for i in range(len(ans)):
            for j in range(k):
                result.append(ans[i])
        return sorted(result)