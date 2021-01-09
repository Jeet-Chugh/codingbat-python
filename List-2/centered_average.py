def centered_average(nums):
  del nums[nums.index(max(nums))]
  del nums[nums.index(min(nums))]
  return sum(nums) // len(nums)
