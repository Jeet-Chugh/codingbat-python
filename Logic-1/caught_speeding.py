def caught_speeding(speed, is_birthday):
  up1, up2, up3, up4 = 60, 61, 80, 81
  if is_birthday:
    up1 += 5
    up2 += 5
    up3 += 5
    up4 += 5
  if speed <= up1:
    return 0
  elif speed >= up2 and speed <= up3:
    return 1
  return 2
