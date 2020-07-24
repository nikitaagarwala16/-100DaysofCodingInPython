'''
Write a function that takes in an array of integers and returns a boolean representing whether the array is monotonic.
An array is said to be monotonic if its elements, from left to right, are entirely non-increasing or entirely non -decreasing.
'''
def monoArray(array):
    arraylen=len(array)
    increasing=True
    decreasing=True
    for i in range(arraylen-1):
      if(array[i+1]>array[i]):
        decreasing=False
      if(array[i+1]<array[i]):
        increasing=False
      if not increasing and not decreasing:
        return False
    return increasing or decreasing
      

if __name__ == "__main__":
  array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
  print(monoArray(array))
