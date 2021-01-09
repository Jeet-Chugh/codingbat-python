def combo_string(a, b):
  long = max([a,b], key=len)
  short = min([a,b], key=len)
  return short + long + short
