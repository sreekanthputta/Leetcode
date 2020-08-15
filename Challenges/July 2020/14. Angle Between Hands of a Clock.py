class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hourAngle = 360*(hour*60+minutes)/(12*60)
        minuteAngle = 360*minutes/60
        
        diff = abs(hourAngle - minuteAngle)
        if(diff>180):
            return 360-diff
        else:
            return diff