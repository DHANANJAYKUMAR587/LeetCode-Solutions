class Solution(object):
    def captureForts(self, forts):
        """
        :type forts: List[int]
        :rtype: int
        """
        arr=[]
        for i in range(len(forts)):
            if forts[i]==1 or forts[i]==-1:
                arr.append(i)
        Ans=[]
        for i in range(len(arr) - 1):
            count=0
            if forts[arr[i]] != forts[arr[i + 1]]:
                for j in range(arr[i] + 1, arr[i + 1]):
                    if forts[j] == 0:
                        count += 1
            Ans.append(count)
        return max(Ans) if Ans else 0