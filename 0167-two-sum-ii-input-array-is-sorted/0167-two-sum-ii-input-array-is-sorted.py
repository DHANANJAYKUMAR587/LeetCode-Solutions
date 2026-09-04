class Solution(object):
    def twoSum(self, num, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i=0
        j=len(num)-1
        while i<j:
            if num[i]+num[j]>target:
                j-=1
            elif num[i]+num[j]<target:
                i+=1
            else:
                return i+1,j+1