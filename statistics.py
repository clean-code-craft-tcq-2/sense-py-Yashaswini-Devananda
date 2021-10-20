
def calculateStats(numbers):
  Calculated_Stats = {}
  if len(numbers)>0:
    Calculated_Stats["avg"] = sum(numbers)/len(numbers)
    Calculated_Stats["max"] = float(max(numbers))
    Calculated_Stats["min"] = float(min(numbers))
  else:
    Calculated_Stats["avg"] = math.nan
    Calculated_Stats["max"] = math.nan
    Calculated_Stats["min"] = math.nan
  return Calculated_Stats
