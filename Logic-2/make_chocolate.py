def make_chocolate(small, big, goal):
  if goal >= 5*big:
    r = goal-5 * big
  else:
    r = goal % 5
  if r <= small:
    return r
  return -1
