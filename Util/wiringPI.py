import wiringpi

wiringpi.wiringPiSetup()

def configureGPIO():
	wiringpi.pinMode(1,1)
	wiringpi.pinMode(4,1)
	wiringpi.pinMode(5,1)
	wiringpi.pinMode(6,1)
	wiringpi.pinMode(26,1)
	wiringpi.pinMode(27,1)
	wiringpi.pinMode(28,1)
	

def readDigSensor(gate):	
	lvlinput = wiringpi.digitalRead(gate)
	return lvlinput

def DigitalWrite(gate, status):
	wiringpi.digitalWrite(gate, status)
	return wiringpi.digitalRead(gate)
