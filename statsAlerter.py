#     emailAlert = EmailAlert()
#     ledAlert = LEDAlert()
#     maxThreshold = 10.5
#     statsAlerter = StatsAlerter(maxThreshold, [emailAlert, ledAlert])
#     statsAlerter.checkAndAlert([22.6, 12.5, 3.7])
#     self.assertTrue(emailAlert.emailSent)
#     self.assertTrue(ledAlert.ledGlows)
import statistics

class EmailAlert():
  emailSent = false
  
class LEDAlert():
  ledGlows = false
 
class StatsAlerter(maxThreshold, listOfAlerts):
  def checkAndAlert(numbers):
    computedStats = statistics.calculateStats(numbers)
    if computedStats["max"] > maxThreshold:
      listOfAlerts[0].emailSent = true
      listOfAlerts[1].ledGlows = true
    else:
      listOfAlerts[0].emailSent = false
      listOfAlerts[1].ledGlows = false
      
     

 

  
