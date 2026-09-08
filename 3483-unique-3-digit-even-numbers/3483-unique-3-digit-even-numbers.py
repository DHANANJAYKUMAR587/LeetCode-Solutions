class Solution(object):
    def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """
        from itertools import permutations
        ans=set()
        for p in permutations(digits,3):
            a=""
            for i in p:
                a+=str(i)
            if a[0]!="0" and int(a)%2==0:
                ans.add(int(a))
        return (len(ans))