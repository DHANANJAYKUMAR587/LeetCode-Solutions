class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """        
        k=k%len(nums)
        i=0
        j=len(nums)-1
        while i<j:
            temp=nums[i]
            nums[i]=nums[j]
            nums[j]=temp
            i+=1
            j-=1
        l=0
        m=k-1
        while l<m:
            temp=nums[l]
            nums[l]=nums[m]
            nums[m]=temp
            l+=1
            m-=1
        f=k
        e=len(nums)-1
        while f<e:
            temp=nums[f]
            nums[f]=nums[e]
            nums[e]=temp
            f+=1
            e-=1
        return nums