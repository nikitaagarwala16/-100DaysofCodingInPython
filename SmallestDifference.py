'''
Sample Input
arrayOne = [-1, 5, 10, 20, 28, 3]
arrayTwo = [26, 134, 135, 15, 17]
Sample Output
[28, 26]
'''
def smallestDifference(arrayOne, arrayTwo):
  arrayOne.sort()
  arrayTwo.sort()
  a=0 
  b=0 
  i=0 
  j=0
  output=[]
  diff=99999
  while a<len(arrayOne) and b< len(arrayTwo):
    if(abs(arrayOne[a]-arrayTwo[b])<diff):
      diff=abs(arrayOne[a]-arrayTwo[b])
      i=a
      j=b
    if(arrayOne[a]<arrayTwo[b]):
      a+=1
    else:
      b+=1
  output.append(arrayOne[i])
  output.append(arrayTwo[j])
  return output
      
    
    
if __name__ == "__main__":
  arrayOne = [-1, 5, 10, 20, 28, 3]
  arrayTwo = [26, 134, 135, 15, 17]
  print(smallestDifference(arrayOne, arrayTwo))
  
  
'''
one appproach is brute force method where we take difference betwen
numbers from both array and find out the minimum
'''
'''
other approach can be using pointers
This algorithm takes O(m log m + n log n) time to sort and O(m + n) time to 
find the minimum difference. Therefore, the overall runtime 
is O(m log m + n log n).
sorting fuction of python uses TimSort and it is an iteration of MergeSort
and its time complexity is O(nlogn)
'''
