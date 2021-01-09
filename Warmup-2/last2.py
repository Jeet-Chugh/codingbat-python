def last2(str):
  return 0 if str == "" else str.count(str[-1:]*3) + str.count(str[-2:])-1
