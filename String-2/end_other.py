def end_other(a, b):
  a,b = a[::-1].lower(), b[::-1].lower()
  return a.startswith(b) or b.startswith(a)
