import serial
import time
import sys

sys.path.append("/usr/local/Projects/INNTIME/Util")
from eventLog import *
from sensorSimulator import *
from wiringPI import *

sys.path.append("/usr/local/Projects/INNTIME/App")
from BLL      import *

try:
	upSensor = 0

	configureGPIO()
	while True:

		lstData = BLL_getPendingData()

		for data in lstData:
			gate = data.split('?')[0]
			status = data.split('?')[1]
			id = data.split('?')[2]

			# SEND COMMAND RPi
			response = DigitalWrite(int(gate), int(status))
			print ('~~~ Sucesso ~~~' if str(status) == str(response) else '~~~Falhou~~~')
								
			# UPDATE ACTION 
			updated_action = BLL_updateActionMobile(id)		
			if(updated_action):
				print "*** Data updated *** "
				print "ID = %s"%id
				print "Status = %s"%status
				print "Gate = %s"%gate

		# SENSOR SIMULATOR
		if(upSensor > 60):
			if(simulatorSensor()):
				upSensor = 0

		time.sleep(1)
		upSensor = upSensor + 1

except Exception,e:
	writeLog("ERROR :: InnTime.py :: %s" %e)
