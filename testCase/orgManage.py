import unittest
from ddt import ddt, data, unpack
from basicMethod.prepareTestData import *


# 保存数据
@ddt
class OrgManageClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        pass

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
        url = server_host + api
        json_data = json.loads(request_data)
        # print("转为json：", json_data)
        if "deleteOrg" in api:
            self.res_data = requests.get(url, headers=header, params=json_data)
            self.assertIn(response_data, self.res_data.text)
        else:
            self.res_data = requests.post(url, headers=header, json=json_data)
            self.assertIn(response_data, self.res_data.text)

    @data(*role_test_data)
    @unpack
    def test_role_manage(self, case_name, api, request_data, response_data):
        url = server_host + api
        json_data = json.loads(request_data)
        # print("=========================")
        # print(json_data)
        # print(type(json_data))
        self.res_data = requests.post(url, headers=header, json=json_data)
        self.assertIn(response_data, self.res_data.text)

    @data(*position_test_data)
    @unpack
    def test_position_manage(self, case_name, api, request_data, response_data):
        url = server_host + api
        json_data = json.loads(request_data)
        # print(json_data)
        if "findAllPosition" in api:
            self.res_data = requests.get(url, headers=header, params=json_data)
            # print(self.res_data)
            self.assertIn(response_data, self.res_data.text)
        elif "dicDetailAdd" in api:
            self.res_data = requests.post(url, headers=header, json=json_data)
            # print(self.res_data)
            self.assertIn(response_data, self.res_data.text)
        elif "updateDicDetail" in api:
            self.res_data = requests.put(url, headers=header, json=json_data)
            # print(self.res_data)
            self.assertIn(response_data, self.res_data.text)
        elif "deleteDir" in api:
            self.res_data = requests.get(url, headers=header, params=json_data)
            # print(self.res_data)
            self.assertIn(response_data, self.res_data.text)
        else:
            print("没有接口：", api)

    @data(*org_user_test_data)
    @unpack
    def test_org_user_manage(self, case_name, api, request_data, response_data):
        url = server_host + api
        json_data = json.loads(request_data)
        # print(json_data)
        if "findOrgUserList" in api:
            self.res_data = requests.get(url, headers=header)
            # print(self.res_data)
            self.assertIn(response_data, self.res_data.text)
        elif "addUser" in api:
            self.res_data = requests.post(url, headers=header, json=json_data)
            # print(self.res_data)
            self.assertIn(response_data, self.res_data.text)
        elif "updateUser" in api:
            self.res_data = requests.post(url, headers=header, json=json_data)
            # print(self.res_data)
            self.assertIn(response_data, self.res_data.text)
        elif "updateStatus" in api:
            self.res_data = requests.post(url, headers=header, json=json_data)
            # print(self.res_data)
            self.assertIn(response_data, self.res_data.text)
        else:
            print("没有接口：", api)


@ddt
class OrderManageClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        pass

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    # def tearDownClass(cls) -> None:
    #     # delData()
    #     pass
    @data(*order_bpmnInstId)
    @unpack
    def test_order_detail(self, case_name, api, request_data, response_data):
        get_order_detail_url = server_host + api
        json_data = json.loads(request_data)
        res_data = requests.post(url=get_order_detail_url, headers=header, json=json_data)
        self.assertIn(response_data, res_data.text)
