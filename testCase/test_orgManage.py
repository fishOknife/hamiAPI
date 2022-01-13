# import unittest
import pytest
import json
import requests
from getConfigInfo import *
# from ddt import ddt, data, unpack
from basicMethod.prepareTestData import get_order_bpmnInstId

order_bpmId = get_order_bpmnInstId()
# print(order_bpmId)
# print(order_bpmId[0])


class Test_OrderManageClass:
    @pytest.mark.parametrize('case_name,api,request_data,response_data', order_bpmId)
    def test_order_detail(self, case_name, api, request_data, response_data):
        # print(case_name)
        # print(api)
        # print(request_data)
        # print(response_data)
        get_order_detail_url = server_host + api
        json_data = json.loads(request_data)
        res_data = requests.post(url=get_order_detail_url, headers=header, json=json_data)

        assert response_data in res_data.text


if __name__ == '__main__':
    # -m 运行指定标记测试方法，-v 输出详细用例执行信息，-k 按照文件名、类名、方法名运行
    pytest.main(["-q orgManage.py"])
