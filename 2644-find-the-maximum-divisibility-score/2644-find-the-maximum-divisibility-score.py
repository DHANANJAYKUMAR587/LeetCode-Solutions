class Solution(object):
    def maxDivScore(self, nums, divisors):
        """
        :type nums: List[int]
        :type divisors: List[int]
        :rtype: int
        """
        ans=[]
        d={}
        for i in range(len(divisors)):
            count=0
            for j in range(len(nums)):
                if nums[j]%divisors[i]==0:
                    count+=1
            d[divisors[i]]=(count)
        a=[]
        max_val = max(d.values())
        for key,val in d.items():
            if val==max_val:
                a.append(key)
        return min(a)