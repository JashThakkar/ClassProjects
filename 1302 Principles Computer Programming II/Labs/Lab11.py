# A small lab where I used numpy and manipulation function that numpy has

import numpy as np

arr = np.full((4, 5), 0)  
arr = np.insert(arr, 1, 7, 0)
arr = np.insert(arr, 1, 5, 1) 
arr = np.delete(arr, 0, 0)  
arr = np.delete(arr, 0, 1)  
arr = np.sort(arr, 0)  
print(np.ravel(arr, order='C'))  
