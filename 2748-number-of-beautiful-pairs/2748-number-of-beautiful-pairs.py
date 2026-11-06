class Solution(object):
    def countBeautifulPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def gcd(a, b):
            while b:
                a,b=b,a%b
            return a
        count=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                a=int(str(nums[i])[0])
                b=nums[j]%10
                if gcd(a,b)==1:
                    count+=1
        return count