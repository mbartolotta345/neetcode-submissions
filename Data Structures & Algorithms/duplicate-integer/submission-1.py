class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # nums.sort()
        # for i in range(len(nums)):
        #     if i == len(nums)-1:
        #         return False
        #     if nums[i] == nums[i+1]:
        #         return True
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            else:
                hashset.add(num)
        return False