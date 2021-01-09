def sum13(nums):
  result, next = [], False
  for i,num in enumerate(nums):
    if (not num == 13 and not next):
      result.append(num)
    elif num == 13:
      next = True
    elif next:
      next = False
  return sum(result)
