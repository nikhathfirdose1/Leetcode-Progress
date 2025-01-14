def twoSum( nums, target):
        hashMap = {}
        for i in range(len(nums)):
            if(target - nums[i] in hashMap):
                return [ hashMap[target - nums[i]], i ]
            hashMap[nums[i]] = i

print(twoSum([2,7,11,15], 9))