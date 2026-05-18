# Python Implementation using a Hash Map
def pair_sum_hash_map(nums, target):
    seen = {} # value -> index
    for index, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], index]
        seen[num] = index
    return []