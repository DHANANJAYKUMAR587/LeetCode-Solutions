class Solution(object):
    def haveConflict(self, event1, event2):
        """
        :type event1: List[str]
        :type event2: List[str]
        :rtype: bool
        """
        if event2[0]<=event1[1] and event1[0]<=event2[1]:
            return True
        return False