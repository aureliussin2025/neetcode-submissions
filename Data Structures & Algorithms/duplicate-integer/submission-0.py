class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checker = set()

        for x in nums:
            checker.add(x)

        if len(checker) != len(nums):
            return True
        else:
            return False
        