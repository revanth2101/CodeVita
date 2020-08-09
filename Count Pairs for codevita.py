#!/usr/bin/env python
# coding: utf-8

# In[1]:


def happyNumbers(arr: list, k: int):
    c_min = arr[0]-k
    c_max = arr[0]+k
    answer = 0
    mergeSort(arr) # nk
    
    for I in range(0, len(arr)): # n
        
            if (arr[I] >= c_min and arr[I] <= c_max):
                answer += 1
            elif (i != 0 and i != len(arr)-1 and (arr[i]-1 >= c_min and arr[i]-1 <= c_max)):
                answer += 1
                
            c_min = arr[i]-k
            c_max = arr[i]+k
            
    return answer


# In[ ]:


def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 # Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 
  
        mergeSort(L) # Sorting the first half 
        mergeSort(R) # Sorting the second half 
  
        I = j = k = 0
          
        # Copy data to temp arrays L[] and R[] 
        while I < len(L) and j < len(R): 
            if L[I] < R[j]: 
                arr[k] = L[i] 
                I+= 1
            else: 
                arr[k] = R[j] 
                j+= 1
            k+= 1
          
        # Checking if any element was left 
        while I < len(L): 
            arr[k] = L[i] 
            I+= 1
            k+= 1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+= 1
            k+= 1

n, k = list(map(int, input().split()))
l = list(map(int, input().split()))
happyNumbers(l, k)


# In[ ]:




