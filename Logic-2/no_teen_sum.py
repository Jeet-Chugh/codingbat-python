def no_teen_sum(a, b, c):
  sum = 0
  for x in [a,b,c]:
    sum += fix_teen(x)
  return sum

def fix_teen(n):
  if n<12 or n > 19 or n in [15,16]:
    return n
  return 0
