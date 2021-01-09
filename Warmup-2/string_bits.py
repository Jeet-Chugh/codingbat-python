def string_bits(str):
  return "".join([x for i,x in enumerate(str) if i%2==0])
