import unittest
import statistics
import math
import alerter
# from alerter import EmailAlert
# from alerter import LEDAlert
# from alerter import StatsAlerter
# import EmailAlert
# import LEDAlert
# import StatsAlerter
import statistics

# class EmailAlert:
#   def __init__(self):
#     self.emailSent = False
    
# #   self.emailSent = False
  
# class LEDAlert:
#   def __init__(self):
#     self.ledGlows = False
# #   ledGlows = False
 
# class StatsAlerter:
#   def __init__(self, maxThreshold, Alerts):
#     self.maxThreshold = maxThreshold
#     self.Alerts = Alerts
    
#   def checkAndAlert(self, numbers):
#     computedStats = statistics.calculateStats(numbers)
#     if computedStats["max"] > self.maxThreshold:
#       self.Alerts[0].emailSent = True
#       self.Alerts[1].ledGlows = True
#     else:
#       self.Alerts[0].emailSent = False
#       self.Alerts[1].ledGlows = False
      
     

class StatsTest(unittest.TestCase):
  def test_report_min_max_avg(self):
    computedStats = statistics.calculateStats([1.5, 8.9, 3.2, 4.5])
    epsilon = 0.001
    self.assertAlmostEqual(computedStats["avg"], 4.525, delta=epsilon)
    self.assertAlmostEqual(computedStats["max"], 8.9, delta=epsilon)
    self.assertAlmostEqual(computedStats["min"], 1.5, delta=epsilon)

  def test_avg_is_nan_for_empty_input(self):
    computedStats = statistics.calculateStats([])
    self.assertTrue(math.isnan(computedStats["avg"]))
    
  def test_max_and_min_is_nan_for_empty_input(self):
    computedStats = statistics.calculateStats([])
    self.assertTrue(math.isnan(computedStats["max"]))
    self.assertTrue(math.isnan(computedStats["min"]))
    # use isnan here
    # All fields of computedStats (average, max, min) must be
    # nan (not-a-number), as defined in the math package
    # Design the assert here.
    # Use nan and isnan in https://docs.python.org/3/library/math.html

  def test_raise_alerts_when_max_above_threshold(self):
    emailAlert = EmailAlert()
    ledAlert = LEDAlert()
    maxThreshold = 10.5
    statsAlerter = StatsAlerter(maxThreshold, [emailAlert, ledAlert])
    statsAlerter.checkAndAlert([22.6, 12.5, 3.7])
    self.assertTrue(emailAlert.emailSent)
    self.assertTrue(ledAlert.ledGlows)

if __name__ == "__main__":
  unittest.main()
