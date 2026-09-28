class Solution(object):
    def mergeArrays(self, nums1, nums2):
        """
        :type nums1: List[List[int]]
        :type nums2: List[List[int]]
        :rtype: List[List[int]]
        """
        ans=[]
        for i in range(len(nums1)):
            a=nums1[i][1]
            for j in range(len(nums2)):
                if nums1[i][0]==nums2[j][0]:
                    a+=nums2[j][1]
            ans.append([nums1[i][0],a])
        for i in range(len(nums2)):
            found=False
            for j in range(len(nums1)):
                if nums2[i][0]==nums1[j][0]:
                    found=True
                    break
            if not found:
                ans.append(nums2[i])
        ans.sort()
        return ans