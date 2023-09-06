class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def function(result, nums, idx):
            if idx == len(nums):
                result.append(nums[:])
                return

            for i in range(idx, len(nums)):
                nums[i],nums[idx] = nums[idx],nums[i]
                function(result, nums, idx + 1)
                nums[i],nums[idx] = nums[idx],nums[i]

        
        function(result, nums[:], 0)
        return result