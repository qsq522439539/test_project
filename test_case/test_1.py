# coding:utf-8
"""
基本的自动化测试脚本 basic_demo.py
"""
import unittest

class TestStringMethods(unittest.TestCase):
	
	def setUp(self):
		print 'init by setUp...'
	
	def tearDown(self):
		print 'end by tearDown...'
	
	def test_upper_caseid1(self):
		u'''大写测试'''
		check = self.assertEqual('foo'.upper(), 'FOO')
	
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
	#执行全部case
	unittest.main()
	##执行部分case
	# testunit = unittest.TestSuite()
	# testunit.addTest(TestStringMethods('test_split'))
	# runner = unittest.TextTestRunner()
	# runner.run(testunit)
