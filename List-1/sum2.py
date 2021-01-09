def sum2(nums):
  return sum(nums) if len(nums) <= 2 else sum(nums[:2])
