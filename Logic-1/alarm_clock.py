def alarm_clock(day, vacation):
  if vacation:
    if day in [6,0]:
      return "off"
    return "10:00"
  if day in [6,0]:
    return "10:00"
  return "7:00"
