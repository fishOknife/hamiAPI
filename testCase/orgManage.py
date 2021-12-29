import json
import requests
import unittest
from ddt import ddt, data, unpack
from basicMethod.basicInfo import *
from basicMethod.useExcel import get_test_data
from basicMethod.useMysql import del_org_data, del_role_data, del_position_data
from basicMethod.basicFunction import *

# 删除数据库中机构、角色、岗位的历史测试数据
del_org_data()
del_role_data()
del_position_data()

# 调用接口添加机构、角色、岗位的默认数据
add_default_org_info()
add_default_role_info()
add_default_position_info()


# 获取修改id后的机构测试数据
org_test_data = change_org_test_info()

# 获取修改id后的角色测试数据
role_test_data = change_role_test_info()

# 获取修改id后的岗位测试数据
position_test_data = change_position_test_info()

# 保存数据
@ddt
class OrgManageClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.header = header

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    # def tearDownClass(cls) -> None:
    #     # delData()
    #     pass

    # 机构管理
    @data(*org_test_data)
    @unpack
    def test_org_manage(self, case_name, api, request_data, response_data):
        url = host + api
        json_data = json.loads(request_data)
        # print("转为json：", json_data)
        if "deleteOrg" in api:
            self.res_data = requests.get(url, headers=self.header, params=json_data)
            self.assertIn(response_data, self.res_data.text)
        else:
            self.res_data = requests.post(url, headers=self.header, json=json_data)
            self.assertIn(response_data, self.res_data.text)

    @data(*role_test_data)
    @unpack
    def test_role_manage(self, case_name, api, request_data, response_data):
        url = host + api
        json_data = json.loads(request_data)
        print("=========================")
        print(json_data)
        print(type(json_data))
        self.res_data = requests.post(url, headers=self.header, json=json_data)
        self.assertIn(response_data, self.res_data.text)

    @data(*position_test_data)
    @unpack
    def test_position_manage(self, case_name, api, request_data, response_data):
        url = host + api
        json_data = json.loads(request_data)
        # print(json_data)
        if "findAllPosition" in api:
            self.res_data = requests.get(url, headers=self.header, params=json_data)
            # print(self.res_data)
            self.assertIn(response_data, self.res_data.text)
        elif "dicDetailAdd" in api:
            self.res_data = requests.post(url, headers=self.header, json=json_data)
            # print(self.res_data)
            self.assertIn(response_data, self.res_data.text)
        elif "updateDicDetail" in api:
            self.res_data = requests.put(url, headers=self.header, json=json_data)
            # print(self.res_data)
            self.assertIn(response_data, self.res_data.text)
        elif "deleteDir" in api:
            self.res_data = requests.get(url, headers=self.header, params=json_data)
            # print(self.res_data)
            self.assertIn(response_data, self.res_data.text)
        else:
            print("没有接口：", api)
