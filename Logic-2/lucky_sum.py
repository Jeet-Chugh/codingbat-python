def lucky_sum(a, b, c):
  l = [a,b,c]
  if 13 in l:
    return sum(l[:l.index(13)])
  return sum(l)
