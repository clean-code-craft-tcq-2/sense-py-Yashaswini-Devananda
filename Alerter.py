#     emailAlert = EmailAlert()
#     ledAlert = LEDAlert()
#     maxThreshold = 10.5
#     statsAlerter = StatsAlerter(maxThreshold, [emailAlert, ledAlert])
#     statsAlerter.checkAndAlert([22.6, 12.5, 3.7])
#     self.assertTrue(emailAlert.emailSent)
#     self.assertTrue(ledAlert.ledGlows)
import statistics

class EmailAlert():
  emailSent = False
  
class LEDAlert():
  ledGlows = False
 
class StatsAlerter():
  def __init__(self, maxThreshold):
    self.maxThreshold = maxThreshold
    
  def checkAndAlert(numbers):
    computedStats = statistics.calculateStats(numbers)
    if computedStats["max"] > self.maxThreshold:
      listOfAlerts[0].emailSent = True
      listOfAlerts[1].ledGlows = True
    else:
      listOfAlerts[0].emailSent = False
      listOfAlerts[1].ledGlows = False
      
     

 

  
