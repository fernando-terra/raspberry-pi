import sys
import random

sys.path.append("/usr/local/Projects/INNTIME/Util")
from eventLog import *
from wiringPI import *

sys.path.append("/usr/local/Projects/INNTIME/App")
from DAL import *

#Region SELECT
def BLL_getPendingData():
	var = []
	try:
		lst = DAL_getPendingData()
		for i in lst:
			_str = str(i[2]) + "?" + str(i[1]) + "?" + str(i[0])
			var.append(_str)
		return var

	except Exception, e:
		writeLog("ERROR :: BLL_getPendingData() at BLL.py :: %s" %e)	

#End Region

#Region INSERT
def BLL_insertSensorSimulator():
	try:
		random_temp = random.randrange(18, 40)
		random_umi = random.randrange(15, 90)

		DAL_insertSensorSimulator(random_temp, random_umi)

		return True

	except Exception, e:
		writeLog("ERROR :: BLL_insertSensorSimulator() at BLL.py :: %s" %e)
#End Region

#Region UPDATE
def BLL_updateActionMobile(ID):
	try:
		DAL_updateActionMobile(ID)
		return True

	except Exception, e:
		writeLog("ERROR :: BLL_updateActionMobile() at BLL.py :: %s " %e)
#End Region
