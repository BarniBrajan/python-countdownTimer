import os
import time as t
import functions as f

clear = lambda: os.system('clear')
userSetHours = f.setUserValue("hours")
userSetMinutes = f.setUserValue("minutes")
userSetSeconds = f.setUserValue("seconds")

userSetValue = userSetHours * 3600 + userSetMinutes * 60 + userSetSeconds 
countDownTime = t.strftime('%H:%M:%S', t.gmtime(userSetValue))

while userSetValue != 0:
    print("Countdown set time: ", countDownTime)
    print(t.strftime('%H:%M:%S', t.gmtime(userSetValue)))
    userSetValue -= 1
    t.sleep(1)
    clear()