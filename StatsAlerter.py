#     emailAlert = EmailAlert()
#     ledAlert = LEDAlert()
#     maxThreshold = 10.5
#     statsAlerter = StatsAlerter(maxThreshold, [emailAlert, ledAlert])
#     statsAlerter.checkAndAlert([22.6, 12.5, 3.7])
#     self.assertTrue(emailAlert.emailSent)
#     self.assertTrue(ledAlert.ledGlows)
import statistics

class EmailAlert():
#    def __init__(self, maxThreshold, Alerts):
#     self.maxThreshold = maxThreshold
  emailSent = False
  
class LEDAlert():
  ledGlows = False
 
class StatsAlerter():
  def __init__(self, maxThreshold, Alerts):
    self.maxThreshold = maxThreshold
    self.Alerts = Alerts
    
  def checkAndAlert(self, numbers):
    computedStats = statistics.calculateStats(numbers)
    if computedStats["max"] > self.maxThreshold:
      self.Alerts[0].emailSent = True
      self.Alerts[1].ledGlows = True
    else:
      self.Alerts[0].emailSent = False
      self.Alerts[1].ledGlows = False
      
     

 

  
