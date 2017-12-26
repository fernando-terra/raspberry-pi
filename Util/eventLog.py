import time
import datetime
import sys

def dateNow():
        return time.asctime(time.localtime(time.time()))

def writeLog(step):

	try:
		file = open("/usr/local/Projects/INNTIME/EventLog/log.txt","a")
	        file.write( dateNow() + ' :: :: ' + step + '\n')
       		file.close()
	except IOError, fileError:
		file = open("/usr/local/INNTIME/log/log.txt","w+")
		print ("Arquivo de log criado com sucesso!")
	except Exception, e:
		print ("Erro com arquivo de log :: %s" %e)
