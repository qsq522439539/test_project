#!/usr/bin/python
# -*- coding: utf-8 -*-
import xmltodict
import paramiko
import json
from xml.dom.minidom import parse

def pythonXmlToJson(xmlStr):
	"""
		demo Python xml to json
	"""
	convertedDict = xmltodict.parse(xmlStr)
	jsonStr = json.dumps(convertedDict, indent=1)
	pythondict = json.loads(jsonStr)
	return  pythondict

def do_clicmd(hostname, username, password, command, port = 22):
	'''
	Set the basic configuration in cli.txt.
	hostname: the conneced host IP address
	username: login host name
	password: login host password
	path: storage path of the configuration script and log
	'''
	port = int(port)
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect(hostname, port, username, password)
	stdin, stdout, stderr = client.exec_command("%s" % command)
	returncode = stdout.read()
	client.close()
	return returncode
	
def getXmlParameter(element, xmlfile="parameters.xml"):
	DOMTree = parse(xmlfile)
	collection = DOMTree.documentElement
	value = collection.getElementsByTagName(element)[0].childNodes[0].data
	return value

if __name__ == "__main__":
	command = "use PCRF; select * from SPR_PCC_RULE where PCC_NAME='Auto';"
	print do_clicmd("192.168.254.121", "root", "baicells",
	      '''mysql -e "use PCRF; select * from SPR_PCC_RULE where PCC_NAME='Auto';"''')
	# print type(do_clicmd("192.168.254.121", "root", "baicells",
	#           "mysql -e 'use PCRF; select * from SPR_PCC_RULE'"))
