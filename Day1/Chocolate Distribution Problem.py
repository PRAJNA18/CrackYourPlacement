def Mindiff(arr, n, m):
    if n == 0 or m == 0:
        return 0
    if n < m:
        return -1
    
    arr.sort()
    min_diff = float('inf')
    i, j = 0, m - 1
    
    while j < n:
        min_diff = min(min_diff, arr[j] - arr[i])
        i += 1
        j += 1
    return min_diff