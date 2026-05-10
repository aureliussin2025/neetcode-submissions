from typing import List # this is used to add type hints for List type

def get_sum(nums: List[int]) -> int:
    total = 0
    for num in nums:
        total += num
    return total
    pass

def get_min(nums: List[int]) -> int:
    curr = 1000
    for num in nums:
        if num < curr:
            curr = num

    return curr
    pass

def get_max(nums: List[int]) -> int:
    curr = 0
    for num in nums:
        if num > curr:
            curr = num

    return curr
    pass

# do not modify below this line
print(get_sum([1, 2, 3, 4, 5]))
print(get_sum([5, 4, 5, 6]))

print(get_min([7, 3, 4, 5]))
print(get_min([5, 4, 5, 6]))

print(get_max([7, 3, 4, 5]))
print(get_max([5, 4, 5, 6]))
