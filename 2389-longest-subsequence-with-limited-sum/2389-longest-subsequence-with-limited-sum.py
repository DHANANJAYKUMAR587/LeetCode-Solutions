class Solution(object):
    def answerQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        nums.sort()
        ans=[]
        for i in queries:
            total=0
            count=0
            for num in nums:
                if total+num<=i:
                    total+=num
                    count+=1
                else:
                    break
            ans.append(count)
        return ans
