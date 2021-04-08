#------------bubble sort---------------#

def sort(array):
    
    for final in range(len(array), 0, -1):
        exchanging = False
        
        for current in range(0, final -1):
             if array[current] > array[current + 1]:
                    array[current + 1], array[current] = array[current], array[current + 1]
                    exchanging = True

        if not exchanging:
            break 
    
    
array = [25, 3, 1, 2, 6, 8, 17, 15, 20, 29, 44, 35, 63]

sort(array)

print(array)