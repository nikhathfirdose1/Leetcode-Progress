def prefixSum(arr, idx):
    prefsum = list()
    prefsum.append(arr[0])

    for i in range(1, idx+1):
        prefsum.append(prefsum[i-1] + arr[i])
    return prefsum[idx]

print(prefixSum([1,1,1,1,1,1,1,1,1,1,1,1],5))
