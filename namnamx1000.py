def nini(arr, s):
    low = 0
    high = len(arr) - 1
    
    while low < high:
        sum = arr[low] + arr[high]
        
        if sum == s:
            return True
        elif sum < s:
            low += 1
        else:
            high -= 1
    
    return False
arr = [3, 5, 10, 22, 59, 94]
s = 104
print(nini(arr, s))