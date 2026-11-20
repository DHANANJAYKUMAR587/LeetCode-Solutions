class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        # ans=[]
        # for i in spells:
        #     pair=[]
        #     for j in potions:
        #         pair.append(i*j)
        #     count=0
        #     for i in pair:
        #         if i>=success:
        #             count+=1
        #     ans.append(count)
        # return ans
        potions.sort()
        m=len(potions)
        ans=[]
        for i in spells:
            target=(success+i-1)//i
            left=0
            right=m
            while left<right:
                mid=(left+right)//2
                if potions[mid]>=target:
                    right=mid
                else:
                    left=mid+1
            ans.append(m-left)
        return ans