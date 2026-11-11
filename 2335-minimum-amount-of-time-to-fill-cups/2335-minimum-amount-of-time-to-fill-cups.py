class Solution(object):
    def fillCups(self, amount):
        """
        :type amount: List[int]
        :rtype: int
        """
        count=0
        while max(amount)>=1:
            a=max(amount)
            amount.remove(a)
            b=max(amount)
            amount.remove(b)
            amount.append(a-1)
            amount.append(b-1)
            count+=1
        return count