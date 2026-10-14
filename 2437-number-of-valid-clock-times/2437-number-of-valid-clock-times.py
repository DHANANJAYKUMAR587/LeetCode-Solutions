class Solution(object):
    def countTime(self, time):
        """
        :type time: str
        :rtype: int
        """
        ans = 1
        if time[0]=='?' and time[1]=='?':
            ans*=24
        elif time[0]=='?':
            ans*=3 if int(time[1])<=3 else 2
        elif time[1]=='?':
            ans*=4 if time[0]=='2' else 10
        if time[3]=='?':
            ans*=6
        if time[4]=='?':
            ans*=10
        return ans