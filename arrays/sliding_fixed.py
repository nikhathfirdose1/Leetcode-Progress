# def max_sum_subarray(nums, k):
#     max_sum = 0
#     window_sum = sum(nums[:k])  # first 3 sum is here 
    
#     for i in range(k, len(nums)): #from 3 to next sums
#         window_sum += nums[i] - nums[i - k]  # add next(idx 3) and subtract prev(idx 0)
#         max_sum = max(max_sum, window_sum)
    
#     return max_sum

# print(max_sum_subarray([1, 2, 3, 4, 5, 6], 3))  # Output: 15


def max_sum_sub(nums, k):
    max_sum = 0
    wind_sum = sum(nums[:k])

    for i in range(k, len(nums)):
        wind_sum += nums[i] - nums[i-k]
        max_sum = max(max_sum, wind_sum)
        print(wind_sum)
    return max_sum

print(max_sum_sub([-1,2,3,1,-3,2], 3))