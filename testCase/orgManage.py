from ddt import ddt, data, unpack
import sys
import json
import unittest
import requests
from basicMethod.useExcel import get_excel_data

# from basicMethod.useMysql import delData

filePath = r"C:\Users\admin\Desktop\哈密\HMAPITest\testData\testData.xlsx"
sheetName = "addOrgInfo"
test_data = get_excel_data(filePath, sheetName)


# print(test_data)


# 保存数据
@ddt
class OrgManageClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # delData()

        cls.header = {
            "X-TENANT-ID": "hami",
            "knfie4j-gateway-request": "0936def8491d5e70510aed4ccd8c5e53",
            "token": "eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJhZG1pbiIsInN1YiI6IntcImFjY291bnRcIjpcImFkbWluXCIsXCJjcmVhdGVkQnlcIjpcInN5c3RlbVwiLFwiY3JlYXRlZERhdGVcIjoxNjMwNTYzMzQzMDAwLFwiaWRcIjoxLFwibG9naW5JZFwiOlwiOTFkZGZkOWUtZmJjOS00ZDdhLWI3OTktZDBiNjEyZGQxMDQ4XCIsXCJvcGVuSWRcIjpcIlwiLFwib3JnSWRcIjozMyxcIm9yZ05hbWVcIjpcIuWTiOWvhumTtuihjFwiLFwicGFzc3dvcmRcIjpcImMzMjg0ZDBmOTQ2MDZkZTFmZDJhZjE3MmFiYTE1YmYzXCIsXCJyb2xlc1wiOlt7XCJpZFwiOjEsXCJyb2xlQ29kZVwiOlwiQURNSU5cIixcInJvbGVOYW1lXCI6XCLnrqHnkIblkZhcIn1dLFwic3RhdHVzXCI6MSxcInRlbmFudElkXCI6XCJEUlNcIixcInR5cGVcIjowLFwidXBkYXRlZEJ5XCI6XCJzeXN0ZW1cIixcInVwZGF0ZWREYXRlXCI6MTYzMDU2MzM0MzAwMCxcInVzZXJOYW1lXCI6XCLotoXnuqfnrqHnkIblkZhcIn0iLCJpc3MiOiJzeXN0ZW0iLCJpYXQiOjE2NDAwNjUzNzYsImV4cCI6MTY0MDE1MTc3Nn0.8zwMScLx6mTCZUylv39jVz0QwXopYsOLPXvxv84NMcg",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome95.0.4638.54 Safari/537.36"
        }

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    # def tearDownClass(cls) -> None:
    #     # delData()
    #     pass
    # 机构管理
    @data(*test_data)
    @unpack
    def test_org_manage(self, case_name, request_url, request_data, response_data):
        json_data = json.loads(request_data)
        self.res_data = requests.post(request_url, headers=self.header, json=json_data)
        self.assertIn(response_data, self.res_data.text)

    # def test001(self):
    #     """获取单条机构信息"""
    #     url = "http://hami-test.tobowork.com:8026/api/v1/system/org/getOne/"
    #     params = {"orgId": "75"}
    #     res = requests.get(url=url, headers=self.header, params=params)
    #     self.assertIn("000000", res.text)
    #
    # def test002(self):
    #     """获取全部机构信息"""
    #     url = "http://hami-test.tobowork.com:8026/api/v1/system/org/listAll"
    #     res = requests.get(url=url, headers=self.header)
    #     self.assertIn("000000", res.text)

    # def test003(self):
    #     """删除单条机构信息"""
    #     url = "http://hami-test.tobowork.com:8026/api/v1/system/org/deleteOrg"
    #     params = {"orgId": "67"}
    #     res = requests.get(url=url, headers=self.header, params=params)
    #     self.assertIn("000000", res.text)

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
