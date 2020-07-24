#You're given an array of integers and an integer. Write a function that moves all instance of that integer in the array to the end of the array and returns the array.
#Write a function that should perform this in place (i.e , it should mutate the input array) and doesn't need too maintain the order of the other integer.
'''
better solution because time complexity is O(n) whereas space complexity
has improved to O(1) which means memory space needed for calculation 
is no longer dependent on the size of the input array.
'''
def moveElementToEnd(array, toMove):
   count=0;
   inputlength=len(array)
   for i in range(inputlength):
     if(array[i]!=toMove):
       array[count]=array[i]
       count+=1
   while(count<inputlength):
     array[count]=toMove
     count+=1
   return array
   


if __name__ == "__main__":
  array = [2, 1, 2, 2, 2, 3, 4, 2]
  toMove = 2
  print(moveElementToEnd(array, toMove))
  
  
# #both tc and sc are o(n)...bad soln
# def moveElementToEnd(array, toMove):
#   inputlength=len(array)
#   outputarray=[]
#   for i in range(0,inputlength):
#     if array[i]==toMove:
#       outputarray.append(toMove)
#     else:
#       outputarray.insert(0,array[i])
#   return outputarray
