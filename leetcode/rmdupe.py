class Solution:
    def __init__(self, nums: list[int]):
        self.nums = nums

    def removeDuplicates(self, nums: list[int]) -> int:
        cool: set = set(nums)
        cool = list(cool)
        return cool
        

nums = [0,0,2,1,1,1,2,3,3,4]
epic = Solution(nums)

print(epic.removeDuplicates(nums))