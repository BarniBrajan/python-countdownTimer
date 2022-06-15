def setUserValue( timeType ):
    while True:        
        userValue = input("Set " + timeType +" time to countdown: ")
        try:
            
            convertedValue = int(userValue)
            return convertedValue
            exit()
        except ValueError:
            print("Bad value, only digits")