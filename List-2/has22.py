def has22(nums):
  return True in [True for i,x in enumerate(nums[:-1]) if x==2 and nums[i+1]==2]
