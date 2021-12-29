# from .testCase.saveData import SaveData
from testCase.orgManage import OrgManageClass
import HTMLTestRunner
import unittest
import time

if __name__ == "__main__":
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    suite.addTest(loader.loadTestsFromTestCase(OrgManageClass))
    # suite.addTest(loader.loadTestsFromTestCase())

    file_prefix = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
    fileName = f"./testReport/{file_prefix}_result.html"

    with open(fileName, "wb") as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="哈密测试报告", description="测试结果", verbosity=2)
        runner.run(suite)
