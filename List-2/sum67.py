def sum67(nums):
  inside = False
  result = 0
  for i in range(len(nums)):
    if nums[i] == 6:
      inside = True
    if not inside:
      result += nums[i]
    if nums[i] == 7 and inside:
      inside = False
  return result
