from sys import argv
import psycopg2
import sys

sys.path.append("/usr/local/Projects/INNTIME/Util")
from decodeConfig import decode
from eventLog import writeLog

sys.path.append("/usr/local/Projects/INNTIME/App")
from DALSQL import *

def connectDB(str):
	try:
		connStr_ = str.split(';')
		conn_ = None

		#Enter the values for you database connection
		dsn_database = connStr_[0]
		dsn_hostname = connStr_[2]
		dsn_port = connStr_[4]
		dsn_uid = connStr_[1]
		dsn_pwd = connStr_[3]

		conn_string = "host="+dsn_hostname+" port="+dsn_port+" dbname="+dsn_database+" user="+dsn_uid+" password="+dsn_pwd
		#print "Connecting to database\n  ->%s" % (conn_string)
		conn_=psycopg2.connect(conn_string)
		#print "Connected!\n"

#		conn_ = psycopg2.connect(database="%s"%connStr_[0],user="%s"%connStr_[1],host="%s"%connStr_[2],password="%s"%connStr_[3], port="%s"%connStr_[4])
		return conn_
	except psycopg2.DatabaseError, e:
		raise ValueError("Connection Failed :: ::  %s" %e)
	
def openConn():
	try:
		connStr = decode()
		conn = None
		conn = connectDB(connStr)
		return conn
	except psycopg2.DatabaseError, e:
		raise ValueError("Connection doesn't open :: %s" %e)


#Region SELECT			
def DAL_getPendingData():
	try:
		conn = None	
		conn = openConn()
		cur = conn.cursor()	
		sqlCmd = DALSQL_getPendingData()
		cur.execute(sqlCmd)
		ver = cur.fetchall()

		return ver

	except Exception, e:
		writeLog("ERROR :: DAL_getPendingData() at DAL.py")
	finally:
		if conn:
			conn.close()
		else:
			writeLog("ERROR :: Connection not Closed at App/DAL.py :: %s" %e)
			
#End Region 

#Region INSERT

def DAL_insertSensorSimulator(temp, umi):
	try:
		conn = openConn()
		cur = conn.cursor()
		sqlCmd = DALSQL_insertSensorSimulator(temp, umi)
		cur.execute(sqlCmd)
		conn.commit()
		
		return True

	except Exception, e:
		writeLog("ERROR :: DAL_insertSensorSimulator() at DAL.py :: %s" %e)
        finally:
		if conn:
			conn.close()
		else:
			writeLog("ERROR :: Connection not Closed at App/DAL.py :: %s" %e)

#End Region

#Region UPDATE
def DAL_updateActionMobile(ID):
	try:
		conn = openConn()
		cur = conn.cursor()
		sqlCmd = DALSQL_updateActionMobile(ID)
		cur.execute(sqlCmd)
		conn.commit()

		return True

	except Exception, e:
		writeLog("ERROR :: DAL_updateActionMobile() at DAL.py :: %s" %e)
	finally:
		if conn:
			conn.close()
		else:
			writeLog("ERROR :: Connection not Closed at App/DAL.py :: %s" %e)
#End Region
