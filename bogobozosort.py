import numpy as np
 
notsorted = True
arr = np.random.rand(np.random.randint(25))

def is_sorted(arr):
    n = len(arr)
    if n <= 1:  # An empty list or a single-element list is considered sorted
        return True
    
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            return False  # Found an unsorted pair
    return True  # All pairs were in order

while notsorted:
    ogarr = arr
    for i in range(len(arr) - 1):
        randomnum1 = np.random.randint(len(arr))
        randomnum2 = np.random.randint(len(arr))
        
        arr[randomnum1], arr[randomnum2] = arr[randomnum2], arr[randomnum1]
        
        print(arr)
        
    if is_sorted(arr) == True:
        notsorted = False
    else:
        arr = ogarr
        
    