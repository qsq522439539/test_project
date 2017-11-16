# coding:utf-8
"""
基本的自动化测试脚本 basic_demo.py
"""
import sys
import unittest
import xmlToJson
import requests

sys.path.append("..")

class TestEpcApi(unittest.TestCase):
	
	def setUp(self):
		print 'init by setUp...'
	
	def tearDown(self):
		print 'end by tearDown...'
	
	def test_QUERY_caseid1(self):
		u'''QUERY查询'''
		xmldata ='''<?xml version="1.0"?>
					<epcOmcPCRF_SPR_PCC_RULE_Req>
					<PROCESS_TYPE>qa</PROCESS_TYPE>
					</epcOmcPCRF_SPR_PCC_RULE_Req>'''
		r = requests.post("http://192.168.254.121:80/epc/om/config_pcrf_spr_pcc_rule.cgi", data=xmldata)
		print (r.text)
	
	def test_isupper_caseid2(self):
		u'''小写测试'''
		self.assertTrue('FOO'.isupper())
		self.assertFalse('Foo'.isupper())
		self.assertTrue('Foo'.isupper())
	
	def test_split_caseid3(self):
		u'''分割测试'''
		s = 'hello world'
		self.assertEqual(s.split(), ['hello', 'world'])
		
if __name__ == '__main__':
	# 执行全部case
	unittest.main()
	# #执行部分case
	# testunit = unittest.TestSuite()
	# testunit.addTest(TestEpcApi('test_isupper_caseid2'))
	# runner = unittest.TextTestRunner()
	# runner.run(testunit)
