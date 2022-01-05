import unittest
from ddt import ddt, data, unpack
from basicMethod.prepareTestData import *
from basicMethod.useMysql import del_org_data, del_role_data, del_position_data, del_org_user_data

# 删除数据库中机构、角色、岗位的历史测试数据
del_org_data()
del_role_data()
del_position_data()
del_org_user_data()

# 调用接口添加机构、角色、岗位的默认数据
add_default_org_info()
add_default_role_info()
add_default_position_info()
add_default_org_user_info()

# 获取修改id后的机构测试数据
org_test_data = change_org_test_info()

# 获取修改id后的角色测试数据
role_test_data = change_role_test_info()

# 获取修改id后的岗位测试数据
position_test_data = change_position_test_info()

# 获取修改id后的机构用户测试数据
org_user_test_data = change_org_user_test_info()

order_bpmnInstId = get_order_bpmnInstId()


# 保存数据
@ddt
class OrgManageClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        pass
        # # 获取到配置文件路径
        # config_path = os.path.dirname(os.getcwd()) + "/config.ini"
        # 
        # # 读取配置文件
        # conf = configparser.ConfigParser()
        # conf.read(config_path, encoding="utf-8")
        # 
        # conf = configparser.ConfigParser()
        # cls.host = conf.get("serverInfo","host")
        # conf.read("config.ini", encoding="utf-8")
        # cls.header = dict(conf.items("header"))

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
        # # 获取到配置文件路径
        # config_path = os.path.dirname(os.getcwd()) + "/config.ini"
        #
        # # 读取配置文件
        # conf = configparser.ConfigParser()
        # conf.read(config_path, encoding="utf-8")
        #
        # conf = configparser.ConfigParser()
        # cls.host = conf.get("serverInfo", "host")
        # conf.read("config.ini", encoding="utf-8")
        # cls.header = dict(conf.items("header"))

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
        # print(get_order_detail_url)
        # print(json_data)
        # data = {
        #     "bpmnInstId": "10000003920283"
        # }
        res_data = requests.post(url=get_order_detail_url, headers=header, json=json_data)
        # print("订单详情：", res_data.text)
        # self.res_data = requests.get(url, headers=header, params=json_data)
        self.assertIn(response_data, res_data.text)

        # url = host + api
        # json_data = json.loads(request_data)
        # # print("转为json：", json_data)
        # if "deleteOrg" in api:
        #     self.res_data = requests.get(url, headers=header, params=json_data)
        #     self.assertIn(response_data, self.res_data.text)
        # else:
        #     self.res_data = requests.post(url, headers=header, json=json_data)
        #     self.assertIn(response_data, self.res_data.text)
