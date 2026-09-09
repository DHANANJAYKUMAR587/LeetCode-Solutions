class Solution(object):
    def accountBalanceAfterPurchase(self, n):
        """
        :type purchaseAmount: int
        :rtype: int
        """
        count=0
        while len(str(n))>1:
            n=n-10
            count+=1
        if n>4:
            count+=1
        return (100-(10*count))