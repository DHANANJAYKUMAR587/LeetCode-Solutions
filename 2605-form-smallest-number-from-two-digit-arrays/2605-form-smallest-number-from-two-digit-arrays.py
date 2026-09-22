class Solution(object):
    def minNumber(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        ans=[]
        for i in nums1:
            if i in nums2:
                ans.append(i)
        if len(ans)==0:
            a=""
            a+=str(min(nums1))
            a+=str(min(nums2))
            a=sorted(a)
            return int("".join(a))
        else:
            return min(ans)