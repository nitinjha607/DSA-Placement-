class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
       # Initial max =-1
       # Reverse iteration
       # New max =max(0ldmax, arr[i])

       rightMax=-1
       for i in range(len(arr)-1,-1,-1):
        newMax= max(rightMax,arr[i])
        arr[i] = rightMax 
        rightMax =newMax
       return arr 
