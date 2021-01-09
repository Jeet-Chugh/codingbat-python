def string_match(a, b):
  short, count = min(len(a), len(b)), 0
  for i in range(short-1):
    if a[i:i+2] == b[i:i+2]:
      count += 1
  return count
