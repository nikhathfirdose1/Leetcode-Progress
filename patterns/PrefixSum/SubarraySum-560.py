def sub_arry_freq(nums, target):
    hm = {0:1}
    key = 0
    freq = 0

    for n in nums:
        key +=n 

        if(key - target in hm):
            freq += hm[key-target]

        hm[key] = hm.get(key, 0) +1 

    return freq

print(sub_arry_freq([1,2,1,2,1], 3))