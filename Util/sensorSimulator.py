import serial
import time
import sys

sys.path.append("/usr/local/Projects/INNTIME/Util")
from eventLog import *

sys.path.append("/usr/local/Projects/INNTIME/App")
from BLL      import *

def simulatorSensor():
	try:
		_return = BLL_insertSensorSimulator()
		upSensor = 0
		if(_return):
			writeLog ("Sensores atualizados! :)")
		else:
			writeLog ("Sensores desatualizados! :(")

		writeLog( "**************************")

		return True

	except Exception, e:
		WriteLog ("ERROR :: simulatorSensor.py :: %s" %e)
