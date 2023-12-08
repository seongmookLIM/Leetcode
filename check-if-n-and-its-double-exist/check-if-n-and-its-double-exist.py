class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
        seen = set()
        
        for i in range(len(arr)):
            if arr[i]*2 in seen:
                return True
            elif arr[i]%2==0 and arr[i]/2 in seen:
                return True
            else:
                seen.add(arr[i])
        return False
        