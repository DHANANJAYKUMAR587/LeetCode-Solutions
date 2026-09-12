class Solution(object):
    def countSpecialIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=[]
        count=0
        for i in nums:
            if nums.count(i)==3 and i not in ans:
                ans.append(i)
        for i in range(len(ans)):
            a=[]
            for j in range(len(nums)):
                if ans[i]==nums[j]:
                    a.append(j)
            if a[1]-a[0]==a[2]-a[1]:
                count+=1
        return count