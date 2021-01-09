def lone_sum(a, b, c):
  l = [a,b,c]
  return sum([x for x in l if l.count(x) == 1])
