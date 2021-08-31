from .testCase.saveData import SaveData
import HTMLTestRunner
import unittest
import time

if __name__ == "__main__":
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    suite.addTest(loader.loadTestsFromTestCase(SaveData))
    # suite.addTest(loader.loadTestsFromTestCase())
    # suite.addTest(loader.loadTestsFromTestCase())
    # suite.addTest(loader.loadTestsFromTestCase())

    file_prefix = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
    fileName = f"./testReport/{file_prefix}_result.html"

    with open(fileName, "wb") as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="标题", description="测试结果", verbosity=2)
        runner.run(suite)
#测试同步代码功能
