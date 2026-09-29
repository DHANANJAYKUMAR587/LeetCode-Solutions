class Solution(object):
    def findTheArrayConcVal(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=[]
        i=0
        j=len(nums)-1
        while i<=j:
            if i==j:
                ans.append(str(nums[i]))
            else:
                ans.append(str(nums[i])+str(nums[j]))
            i+=1
            j-=1
        total=0
        for i in ans:
            total+=int(i)
        return total