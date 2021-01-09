def round_sum(a, b, c):
  sum = 0
  for x in [a,b,c]:
    sum += round10(x)
  return sum

def round10(n):
  l_dig = int(str(n)[-1])
  if l_dig >= 5:
    return n + 10-l_dig
  return n-l_dig
