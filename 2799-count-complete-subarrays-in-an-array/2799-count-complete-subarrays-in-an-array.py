class Solution(object):
    def countCompleteSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        total=len(set(nums))
        for i in range(len(nums)):
            seen = set()
            for j in range(i, len(nums)):
                seen.add(nums[j])
                if len(seen) == total:
                    count += 1
        return count