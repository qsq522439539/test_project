# coding:utf-8
"""
基本的自动化测试脚本 basic_demo.py
"""
import sys
import re
import unittest
import requests
from common import *

sys.path.append("..")

class TestEpcApi(unittest.TestCase):
	
	def setUp(self):
		print 'init by setUp...'
		self.ssh_root_user = getXmlParameter("ssh_root_user")
		self.ssh_root_key = getXmlParameter("ssh_root_key")
		self.ssh_port = getXmlParameter("ssh_port")
		self.ssh_epc_ip = getXmlParameter("ssh_epc_ip")
		self.ssh_epc_user = getXmlParameter("ssh_epc_user")
		self.ssh_epc_passwd = getXmlParameter("ssh_epc_passwd")
		
	def tearDown(self):
		print 'end by tearDown...'
	
	# @unittest.skip("")
	def test_QUERY_caseid1(self):
		u'''QUERY测试'''
		xmldata = '''<?xml version="1.0"?>
					<epcOmcPCRF_SPR_PCC_RULE_Req>
					<PROCESS_TYPE>qa</PROCESS_TYPE>
					</epcOmcPCRF_SPR_PCC_RULE_Req>'''
		r = str(requests.post("http://192.168.254.121:80/epc/om/config_pcrf_spr_pcc_rule.cgi", data=xmldata))
		status = re.findall(r"Response \[(\d{3})\]",r)[0]
		self.assertEqual(status,"200")
		
	# @unittest.skip("")
	def test_ADD_caseid2(self):
		u'''ADD测试'''
		xmldata ='''<?xml version="1.0"?>
<epcOmcPCRF_SPR_PCC_RULE_Req>
	<PROCESS_TYPE>pp</PROCESS_TYPE>
	<ITEM>
		<OPER_TYPE>A</OPER_TYPE>
		<PCC_NAME>Auto</PCC_NAME>
		<QCI>2</QCI>
		<ARP_PL>2</ARP_PL>
		<ARP_PCI>1</ARP_PCI>
		<ARP_PVI>1</ARP_PVI>
		<MBR_UL>1024000</MBR_UL>
		<MBR_DL>5120000</MBR_DL>
		<GBR_UL>1024000</GBR_UL>
		<GBR_DL>1024000</GBR_DL>
		<PRECEDENCE>0</PRECEDENCE>
		<PF_LIST>200</PF_LIST>
	</ITEM>
</epcOmcPCRF_SPR_PCC_RULE_Req>'''
		r = str(requests.post("http://192.168.254.121:80/epc/om/config_pcrf_spr_pcc_rule.cgi", data=xmldata))
		status = re.findall(r"Response \[(\d{3})\]", r)[0]
		self.assertEqual(status, "200")
		mysqldata = do_clicmd(self.ssh_epc_ip, self.ssh_epc_user, self.ssh_epc_passwd,
		           '''mysql -e "use PCRF; select * from SPR_PCC_RULE where PCC_NAME='Auto';"''')
		mysqldata = mysqldata.split('\n')[1]
		self.assertEqual("Auto	2	2	1	1	1024000	5120000	1024000	1024000	0	200", mysqldata)
	
	# @unittest.skip("")
	def test_UPDATE_caseid3(self):
		u'''UPDATE测试'''
		xmldata = '''<?xml version="1.0"?>
		<epcOmcPCRF_SPR_PCC_RULE_Req>
			<PROCESS_TYPE>pp</PROCESS_TYPE>
			<ITEM>
				<OPER_TYPE>A</OPER_TYPE>
				<PCC_NAME>Auto</PCC_NAME>
				<QCI>2</QCI>
				<ARP_PL>2</ARP_PL>
				<ARP_PCI>1</ARP_PCI>
				<ARP_PVI>1</ARP_PVI>
				<MBR_UL>1024000</MBR_UL>
				<MBR_DL>5120000</MBR_DL>
				<GBR_UL>1024000</GBR_UL>
				<GBR_DL>1024000</GBR_DL>
				<PRECEDENCE>0</PRECEDENCE>
				<PF_LIST>200</PF_LIST>
			</ITEM>
		</epcOmcPCRF_SPR_PCC_RULE_Req>'''
		r = str(requests.post("http://192.168.254.121:80/epc/om/config_pcrf_spr_pcc_rule.cgi", data=xmldata))
		status = re.findall(r"Response \[(\d{3})\]", r)[0]
		self.assertEqual(status, "200")
		xmldata2 = '''<?xml version="1.0"?>
<epcOmcPCRF_SPR_PCC_RULE_Req>
	<PROCESS_TYPE>pp</PROCESS_TYPE>
	<ITEM>
		<OPER_TYPE>M</OPER_TYPE>
		<PCC_NAME>Auto</PCC_NAME>
		<QCI>1</QCI>
		<ARP_PL>3</ARP_PL>
		<ARP_PCI>1</ARP_PCI>
		<ARP_PVI>1</ARP_PVI>
		<MBR_UL>1024000</MBR_UL>
		<MBR_DL>5120000</MBR_DL>
		<GBR_UL>1024000</GBR_UL>
		<GBR_DL>10240400</GBR_DL>
		<PRECEDENCE>0</PRECEDENCE>
		<PF_LIST>2</PF_LIST>
	</ITEM>
</epcOmcPCRF_SPR_PCC_RULE_Req>'''
		r = str(requests.post("http://192.168.254.121:80/epc/om/config_pcrf_spr_pcc_rule.cgi", data=xmldata2))
		status = re.findall(r"Response \[(\d{3})\]", r)[0]
		self.assertEqual(status, "200")
		mysqldata = do_clicmd(self.ssh_epc_ip, self.ssh_epc_user, self.ssh_epc_passwd,
		           '''mysql -e "use PCRF; select * from SPR_PCC_RULE where PCC_NAME='Auto';"''')
		mysqldata = mysqldata.split('\n')[1]
		print mysqldata
		self.assertEqual("Auto	1	3	1	1	1024000	5120000	1024000	10240400	0	2", mysqldata)
	
	# @unittest.skip("")
	def test_DELETE_caseid4(self):
		u'''DELETE测试'''
		xmldata = '''<?xml version="1.0"?>
<epcOmcPCRF_SPR_PCC_RULE_Req>
	<PROCESS_TYPE>pp</PROCESS_TYPE>
	<ITEM>
		<OPER_TYPE>d</OPER_TYPE>
		<PCC_NAME>Auto</PCC_NAME>
	</ITEM>
</epcOmcPCRF_SPR_PCC_RULE_Req>'''
		r = str(requests.post("http://192.168.254.121:80/epc/om/config_pcrf_spr_pcc_rule.cgi", data=xmldata))
		status = re.findall(r"Response \[(\d{3})\]", r)[0]
		self.assertEqual(status, "200")
		mysqldata = do_clicmd(self.ssh_epc_ip, self.ssh_epc_user, self.ssh_epc_passwd,
		                      '''mysql -e "use PCRF; select * from SPR_PCC_RULE where PCC_NAME='Auto';"''')
		self.assertEqual('', mysqldata)
