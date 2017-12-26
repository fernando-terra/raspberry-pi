import sys
sys.path.append("/usr/local/Projects/INNTIME/Util")
from eventLog import writeLog

#Region SELECT
def DALSQL_getPendingData():
	try:
		sqlCmd  = ' SELECT ACT.ID, '
#		sqlCmd += '	   ACT.OBJECT_ID, '
		sqlCmd += '    	   ACT.ENABLED, '
		sqlCmd += '        OBJ.GATE '
		sqlCmd += ' FROM INNT.ACTION ACT'
		sqlCmd += ' INNER JOIN INNT.OBJECTS OBJ ON OBJ.ID = ACT.OBJECT_ID'
		sqlCmd += ' WHERE ACT.PROCESSDATE IS NULL '
		sqlCmd += ' ORDER BY ACT.CREATIONDATE ASC '

		return sqlCmd

	except Exception, e:
		writeLog("ERROR :: DALSQL_getPendingData() at DALSQL.py :: %s" %e)		
#End Region

#Region INSERT

def DALSQL_insertSensorSimulator(temp, umi):
	try:
		sqlCmd  = " INSERT INTO INNT.MONITOR "
		sqlCmd += " VALUES (NEXTVAL('SERIAL_MONITOR') "
		sqlCmd += " 	   ,CURRENT_TIMESTAMP "
		sqlCmd += " 	   ,3  " 
		sqlCmd += "	   ,%s " %umi
		sqlCmd += " 	   ,%s " %temp
		sqlCmd += "	   )"

		return sqlCmd

	except Exception, e:
		writeLog("ERROR :: DALSQL_insertSensorSimulator() at DALSQL.py :: %s" %e)	


#End Region

#Region UPDATE
def DALSQL_updateActionMobile(ID):
	try:
		sqlCmd  = ' UPDATE INNT.ACTION SET PROCESSDATE = CURRENT_TIMESTAMP WHERE ID = %s ' %ID
		return sqlCmd

	except Exception, e:
		writeLog("ERROR :: DALSQL_updateActionMobile() at DALSQL.py :: %s" %e)
#End Region
