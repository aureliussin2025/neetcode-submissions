class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr) - 2
        curr = 0
        temp = arr[len(arr) - 1]
        while n >= 0:
            
            curr = max(curr, temp)
            temp = arr[n]
            arr[n] = curr
            
            n -= 1
            
            
        arr[len(arr) - 1] = -1
        return arr
        