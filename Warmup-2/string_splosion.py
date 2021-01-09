def string_splosion(str):
  result, current = "", ""
  for char in str:
    current += char
    result += current
  return result
