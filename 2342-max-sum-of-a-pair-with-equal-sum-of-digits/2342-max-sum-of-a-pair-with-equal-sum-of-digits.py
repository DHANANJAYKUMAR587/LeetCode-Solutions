class Solution(object):
    def maximumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def Sum(n):
            a=str(n)
            b=list(a)
            t=0
            for i in b:
                t+=int(i)
            return t
        # ans=[]
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if Sum(nums[i])==Sum(nums[j]):
        #             ans.append(nums[i]+nums[j])
        # Max=-1
        # for i in ans:
        #     if i>Max:
        #         Max=i
        # return Max
        Max=-1
        d={}
        for i in range(len(nums)):
            s=Sum(nums[i])
            if s in d:
                Max=max(Max,nums[i]+d[s])
                if nums[i]>d[s]:
                    d[s]=nums[i]
            else:
                d[s]=nums[i]
        return Max