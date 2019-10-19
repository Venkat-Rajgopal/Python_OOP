# given an array of integers find duplicates in them
# input: nums = [7,6,4,3,1,1]
# output: True

# Normal approach - O(n) time, O(1) space
def containsDuplicate(nums):
    seen = []

    for item in nums:
        
        if item in seen:
            return True
        else:
            seen.append(item)   # first number is added to the seen list and then every other is compared
    return False

containsDuplicate(nums)