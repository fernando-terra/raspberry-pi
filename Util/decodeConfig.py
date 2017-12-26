import sys
from sys import argv

def decode():

	try:

        	#Reading Config File
	        appconfig  = open("/usr/local/Projects/INNTIME/Config/app.config")
	        file  = appconfig.read()
		lst = file.split('|')
		var = lst[1]

		return var

	except Exception, e:
		print ("ERROR :: decode at decodeConfig.py ::: %s"%e)
