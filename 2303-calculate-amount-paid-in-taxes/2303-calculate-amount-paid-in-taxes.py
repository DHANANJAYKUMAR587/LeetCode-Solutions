class Solution(object):
    def calculateTax(self, brackets, income):
        """
        :type brackets: List[List[int]]
        :type income: int
        :rtype: float
        """
        ans=[]
        ans.append(brackets[0][0])
        for i in range(len(brackets)-1):
            ans.append(brackets[i+1][0]-brackets[i][0])
        result=[]
        for i in range(len(ans)):
            if ans[i]<=income:
                income=income-ans[i]
                result.append(ans[i])
            else:
                result.append(income)
                income = 0
        per=[]
        for i in brackets:
            per.append(i[1])
        Ans=[]
        for i in range(len(result)):
            Ans.append((result[i]*per[i])/100.0)
        return (sum(Ans))