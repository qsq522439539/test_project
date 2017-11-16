# coding=utf-8

import re
import time
import unittest
import HTMLTestRunner
import testlink
from test_case.test_epc import *
test_dir = r"C:\Users\admin\PycharmProjects\test_project\test_case"
report_dir = r"C:\Users\admin\PycharmProjects\test_project\report\Autotest_"
testlink_url = "http://192.168.5.9:9080/testlink/lib/api/xmlrpc/v1/xmlrpc.php"
testlink_devkey = "f1d400e885496d59fb0ac5cc9f6f506a"
test_plan_id = ""
buidname = ""
username = ""
debug = 0

def creatsuite():
    testunit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(test_dir, pattern="test*.py")
    
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            print(testunit)
    return testunit

def FillResultToTestLink(test_result, test_case_id):  #qsq 10.27
    myTestLink = testlink.TestlinkAPIClient(testlink_url, testlink_devkey)
    newResult = myTestLink.reportTCResult(test_case_id, test_plan_id , buidname,
                                          test_result, "Autotest", bugid='',
                                          user=username)
    print("reportTCResult", newResult)
        
if __name__=='__main__':
    alltestnames = creatsuite()
    casename = re.findall("testMethod=test_(.*?)>",str(alltestnames))
    all_case_id = []
    for c in casename:
        all_case_id.append(c.split("_")[-1])
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = report_dir + now + "_Result.html"
    fp = open(filename, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u'自动化测试报告',
                                           description=u'自动化测试报告',
                                           verbosity=2)
    test_result = runner.run(alltestnames)
    fp.close()
    print('All case number: %s'%test_result.testsRun)
    print('Successed case number: %s' % test_result.success_count)
    print('Failed case number: %s'%len(test_result.failures))
    if debug:
        for case, reason in test_result.failures:
            fail_case_id = case.id().split(".")[-1].split("_")[-1]
            all_case_id.remove(fail_case_id)
            FillResultToTestLink("f", fail_case_id)
        for success_case_id in all_case_id:
            FillResultToTestLink("p", success_case_id)

