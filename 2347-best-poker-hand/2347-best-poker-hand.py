class Solution(object):
    def bestHand(self, ranks, suits):
        """
        :type ranks: List[int]
        :type suits: List[str]
        :rtype: str
        """
        if len(set(suits))==1:
            return "Flush"
        elif max(ranks.count(i) for i in set(ranks))>=3:
            return "Three of a Kind"
        elif len(set(ranks))<=4:
            return "Pair"
        else:
            return "High Card"