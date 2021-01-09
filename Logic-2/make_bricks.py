def make_bricks(small, big, goal):
  if goal >= 5*big:
      r = goal - (5*big)
  else:
      r = goal % 5
  return small >= r
