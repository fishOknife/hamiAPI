import unittest
import requests
from basicMethod.useExcel import getExcelData
from basicMethod.useMysql import delData


class saveData(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        delData()
        filePath = r".\testData\testData.xlsx"
        sheetName = "保存"
        cls.test_data = getExcelData(filePath, sheetName)
        cls.header = {
            "User-Agent": "Mozilla / 5.0(Windows NT 6.1;",
            "Cookie": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
        }

    def setUp(self) -> None:
        # 执行一条测试用例，就将列表中的第一条数据pop出来
        self.oneCase = self.test_data.pop(0)
        self.requestUrl = self.oneCase["url"]
        self.requestData = self.oneCase["requestData"]
        self.responseData = self.oneCase["responseData"]

    def tearDown(self) -> None:
        pass

    def tearDownClass(cls) -> None:
        delData()
        # pass

    def test001(self):
        """姓名为空"""
        self.resData = requests.post(self.requestUrl, header=self.header, json=self.requestData)
        self.assertIn(self.responseData, self.resData.text)

    def test002(self):
        """电话为空"""
        self.resData = requests.post(self.requestUrl, header=self.header, json=self.requestData)
        self.assertIn(self.responseData, self.resData.text)

    def test003(self):
        """性别为空"""
        self.resData = requests.post(self.requestUrl, header=self.header, json=self.requestData)
        self.assertIn(self.responseData, self.resData.text)

    def test004(self):
        """正向用例"""
        self.resData = requests.post(self.requestUrl, header=self.header, json=self.requestData)
        self.assertIn(self.responseData, self.resData.text)
