def min_subarray_sum(nums, target):
    left = 0
    min_length = float('inf')
    current_sum = 0

    for right in range(len(nums)): # right is updated here
        current_sum += nums[right]
        while current_sum >= target:  # wont check sum unless it is = or higher than target present
            min_length = min(min_length, right - left + 1) #right - left is for the length at which value was found +1 for adjustment
            current_sum -= nums[left] # shrink it by removing left 
            left += 1 # update left 

    return min_length if min_length != float('inf') else 0 # to get subarray length
    # return nums[left-1: right+1] # to get the array 

# print(min_subarray_sum([2, 3, 1, 2, 4, 3], 7))  # Output: 2 [4,3]

def max_subarray_length(nums, target):
    left = 0
    max_length = 0
    current_sum = 0

    for right in range(len(nums)):
        current_sum += nums[right]



        while current_sum >= target:
            max_length = max(max_length, right - left + 1)  # update the length coz hit target in prev condition
            current_sum -= nums[left]  # Shrink window next
            left += 1


    return max_length

nums = [1, 2, 3, 4, 5]
target = 10
print(max_subarray_length(nums, target))  # Output: 4 (subarray [2, 3, 4, 1])

# max subarray shrinkk first then update max_len -> this approach solution is below

def max_length_subarray(nums, target):
    left = 0
    window_sum = 0
    max_length = 0

    for right in range(len(nums)):
        window_sum += nums[right]

        while window_sum > target:  # Breaks condition, here sum is beyond target value
            window_sum -= nums[left]  # Shrink first
            left += 1

        max_length = max(max_length, right - left + 1)  # Then update

    return max_length
