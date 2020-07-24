'''
Given an array arr[] with N elements, the task is to find out the longest sub-array which has the shape of a mountain.
The Longest Peak consists of elements that are initially in ascending order until a peak element is reached and beyond 
the peak element all other elements of the sub-array are in decreasing order.
'''
def LongestPeak(a): 
  # Write your code here
  result=0
  alength=len(a)
  if(alength<3):#if the length of the array is less than 3 wwe cannot find longest sub peak
    return 0
  else:
    left=0
    while(left<alength-2):
      while(left<alength-1 and a[left]>a[left+1]):#find the starting of the sub array
        left+=1
      right=left+1
      while right<alength-1 and a[right]<a[right+1]:#to check increasing behaviour
        right+=1 
      while right<alength-1 and a[right]>a[right+1]: #to check decreasing behaviour
        right+=1 
        result=max(result,right-left+1)
      left=right
        
  return result
  


if __name__ == "__main__":
  d = [ 1, 3, 1, 4, 5, 6,  
        7, 8, 9, 8, 7, 6, 5 ]
  print(LongestPeak(d)) 
      
