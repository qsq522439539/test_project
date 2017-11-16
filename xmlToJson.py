#!/usr/bin/python
# -*- coding: utf-8 -*-
import xmltodict
import json

def pythonXmlToJson(xmlStr):
	"""
		demo Python xml to json
	"""
	convertedDict = xmltodict.parse(xmlStr)
	jsonStr = json.dumps(convertedDict, indent=1)
	PythonStr = json.loads(jsonStr)
	print "jsonStr=", jsonStr
	print "PythonStr=", PythonStr
	return  jsonStr, PythonStr

# if __name__ == "__main__":
	# dictVal1 = pythonXmlToJson()