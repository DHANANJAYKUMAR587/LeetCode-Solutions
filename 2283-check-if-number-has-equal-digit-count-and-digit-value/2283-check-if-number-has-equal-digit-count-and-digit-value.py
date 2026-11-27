class Solution(object):
    def digitCount(self, num):
        """
        :type num: str
        :rtype: bool
        """
        nums=[]
        ans=[]
        Bool=True
        for i in num:
            nums.append(int(i))
        for i in range(len(nums)):
            if nums.count(i)!=nums[i]:
                Bool=False
        return Bool