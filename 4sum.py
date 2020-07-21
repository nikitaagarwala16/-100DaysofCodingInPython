"""
Sample Input
array = [7,6,4,-1,1,2]
targetSum = 16

Sample Output
// the quadruplets could be ordered differently
[7, 6, 4, -1], [7, 6, 1, 2]]"""

def fourNumberSum(array, targetSum):
  array.sort()
  inputlen=len(array)
  outputarray=[]
  for i in range(0,inputlen):
    for j in range(i+1,inputlen):
      left=j+1
      right=inputlen-1
      while(left<right):
        total=array[i]+array[j]+array[left]+array[right]
        if(total==targetSum):
          outputarray.append([array[right],array[left],array[j],array[i]])
          left+=1
          right-=1
        elif total>targetSum :
          right-=1
        elif total<targetSum:
          left+=1
      while j+1<inputlen and array[j]==array[j+1] :
        j+=1
    while i+1<inputlen and array[i]==array[i+1] :
        i+=1

  return outputarray

  
  
if __name__ == "__main__":
  array = [7,6,4,-1,1,2]
  targetSum = 16
  output = fourNumberSum(array, targetSum)
  print(output)
  
#TC is O(n^2)
