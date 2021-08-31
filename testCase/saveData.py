from ddt import ddt, data, unpack
import sys
import unittest
import requests
from basicMethod.useExcel import get_excel_data
from basicMethod.useMysql import delData

rootDir = sys.path[1]
filePath = rootDir + r"\testData\testData.xlsx"
sheetName = "保存"
test_data = get_excel_data(filePath, sheetName)


# 保存数据
@ddt
class SaveData(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        delData()
        # filePath = r".\testData\testData.xlsx"
        # sheetName = "保存"
        # cls.test_data = get_excel_data(filePath, sheetName)
        cls.header = {
            "User-Agent": "Mozilla / 5.0(Windows NT 6.1;",
            "Cookie": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
        }

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def tearDownClass(cls) -> None:
        delData()
        # pass

    @data(*test_data)
    @unpack
    def test001(self, request_url, request_data, response_data):
        """姓名为空"""
        self.resData = requests.post(request_url, header=self.header, json=request_data)
        self.assertIn(response_data, self.resData.text)

    # def test001(self):
    #     """姓名为空"""
    #     self.resData = requests.post(self.requestUrl, header=self.header, json=self.requestData)
    #     self.assertIn(self.responseData, self.resData.text)
    #
    # def test002(self):
    #     """电话为空"""
    #     self.resData = requests.post(self.requestUrl, header=self.header, json=self.requestData)
    #     self.assertIn(self.responseData, self.resData.text)
    #
    # def test003(self):
    #     """性别为空"""
    #     self.resData = requests.post(self.requestUrl, header=self.header, json=self.requestData)
    #     self.assertIn(self.responseData, self.resData.text)
    #
    # def test004(self):
    #     """正向用例"""
    #     self.resData = requests.post(self.requestUrl, header=self.header, json=self.requestData)
    #     self.assertIn(self.responseData, self.resData.text)
