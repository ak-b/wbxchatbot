import re
import click

def filecleanup(input):
	f = open("/Users/akbansal/wibot/files/device_log.txt","w")
	f.write(input)
	with open('/Users/akbansal/wibot/files/device_log.txt','r') as file:
		linelist = file.readlines()
		for lines in linelist:
			if lines.startswith('CPU'):
				sys.stdout.write(lines)
				

def cpu_process(input):
	filecleanup(input)

	