class Solution(object):
    def countSeniors(self, details):
        """
        :type details: List[str]
        :rtype: int
        """
        count=0
        for i in details:
            a=""
            a+=i[11]
            a+=i[12]
            if int(a)>60:
                count+=1
        return count