class Solution(object):
    def mergeSimilarItems(self, items1, items2):
        """
        :type items1: List[List[int]]
        :type items2: List[List[int]]
        :rtype: List[List[int]]
        """
        ans=[]
        for i in range(len(items1)):
            for j in range(len(items2)):
                if items1[i][0]==items2[j][0]:
                    ans.append([items1[i][0],items1[i][1]+items2[j][1]])
        t=[]
        a=[]
        for i in range(len(items2)):
            t.append(items2[i][0])
        for i in range(len(items1)):
            if items1[i][0] not in t:
                a.append(items1[i])  
        result=[]
        for i in ans:
            result.append(i)
        for i in a:
            result.append(i)
        r=[]
        for i in range(len(result)):
            r.append(result[i][0])
        for i in range(len(items2)):
            if items2[i][0] not in r:
                result.append(items2[i])
        return sorted(result)