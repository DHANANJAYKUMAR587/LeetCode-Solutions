class Solution(object):
    def pickGifts(self, gifts, k):
        """
        :type gifts: List[int]
        :type k: int
        :rtype: int
        """
        import math
        while k!=0:
            a=max(gifts)
            b=int(math.sqrt(a))
            gifts.remove(a)
            gifts.append(b)
            k-=1
        return sum(gifts)