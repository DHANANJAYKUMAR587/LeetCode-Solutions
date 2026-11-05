class Solution(object):
    def countBadPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        freq={}
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if (i<j) and (i-j!=nums[i]-nums[j]):
        #             count+=1
        for i in range(len(nums)):
            key=i-nums[i]
            count+=i-freq.get(key,0)
            freq[key]=freq.get(key,0)+1
        return count