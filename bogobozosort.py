import numpy as np
 
def is_sorted(arr):
    n = len(arr)
    if n <= 1:  # An empty list or a single-element list is considered sorted
        return True
    
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            return False  # Found an unsorted pair
    return True  # All pairs were in order

def bogobozosort(arr, print_logs):
    while True:
        og_arr = arr.copy()
        for i in range(len(arr) - 1):
            randomnum1 = np.random.randint(len(arr))
            randomnum2 = np.random.randint(len(arr))

            arr[randomnum1], arr[randomnum2] = arr[randomnum2], arr[randomnum1]

            if print_logs:
                print(arr)

        if is_sorted(arr):
            return arr
        else:
            arr = og_arr
import numpy as np
 

    