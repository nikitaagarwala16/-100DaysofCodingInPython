#!/usr/bin/env python
# coding: utf-8

# In[1]:


def bool2str(m_bool):
  if m_bool:
    return 'true'
  else:
    return 'false'
    
def isValidSubsequence(array, sequence):
    is_valid = False
    array_length=len(array)
    sequence_length=len(sequence)
    i=0 
    j=0 
    while i<array_length and j<sequence_length:
      if array[i]==sequence[j]:
        j+=1
      i+=1
    if j==sequence_length:# means entire sequence was found in the array
      is_valid=True
      
    return bool2str(is_valid)
  
  
if __name__ == "__main__":
  array = [ 5, 1, 22, 5, 6, -1, 8, 10]
  subsequence = [1, 6, -1, 10]
  print(isValidSubsequence(array, subsequence))
  


# In[ ]:




