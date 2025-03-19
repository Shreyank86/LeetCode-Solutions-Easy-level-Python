def miniMaxSum(arr):
    arr = sorted(arr)
    sum = 0
    mini = 0
    n = len(arr)
    for i in range(n) :
        sum += arr[i]
    
    maxi = sum - arr[0]
    mini = sum - arr[-1]
    print(mini , maxi)