import json
import requests
from getConfigInfo import *
# from basicMethod.useMysql import query_id_from_table
from basicMethod.useExcel import get_excel_data, get_dict_data, get_test_data
from basicMethod.useMysql import DelDBData

# 删除数据库中机构、角色、岗位的历史测试数据
DelDBData.del_org_data()
DelDBData.del_role_data()
DelDBData.del_position_data()
DelDBData.del_org_user_data()


# 调接口插入初始数据
class AddDefaultData:
    @staticmethod
    def add_default_list_data(url, sheet_name):
        # 从excel中获取数据
        one_org_info = get_excel_data(defaultTestDataFile, sheet_name)
        for i in range(0, len(one_org_info)):
            res = requests.post(url, headers=header, json=one_org_info[i])
            print(f"调接口插入{sheet_name}数据：", res.text)

    @staticmethod
    def add_default_dict_data(url, sheet_name):
        # 从excel中获取数据
        one_role_info = get_dict_data(defaultTestDataFile, sheet_name)
        for i in range(0, len(one_role_info)):
            json_data = json.loads(one_role_info[i])
            res = requests.post(url, headers=header, json=json_data)
            print(f"调接口插入{sheet_name}数据：", res.text)


# 根据传入的字段查询id，并将查询回来的id写入测试数据中
def change_test_data_id(table_name, table_field, field_list, sheet_name):
    # 修改机构ID
    restore_list = []
    id_list = DelDBData.query_id_from_table(table_name, table_field, field_list)
    # 从excel中查询测试数据，保存至列表中
    change_id_data = get_test_data(testDataFile, sheet_name)
    for i in range(0, len(change_id_data)):
        one_data = change_id_data.pop(0)
        # 判断是否为编辑，因为编辑需要根据ID修改
        if "update" in one_data[1]:
            # print("修改id前的数据：", one_data)
            # 提取需要修改ID的数据，并转为dict
            one_test_data = eval(one_data.pop(2))
            # print("ID列表：", id_list)
            # 从ID列表中获取一条ID替换原ID
            one_test_data["id"] = id_list.pop(0)
            # print(type(one_test_data))
            # 将修改后的数据插入到列表中
            dict2json = json.dumps(one_test_data, ensure_ascii=False)
            one_data.insert(2, dict2json)
            # print("修改id后的数据：", one_data)
            restore_list.append(one_data)
        elif "del" in one_data[1]:
            one_test_data = eval(one_data.pop(2))
            if "deleteOrg" in one_data[1]:
                one_test_data["orgId"] = id_list.pop(0)
                # print("一条完整的删除数据：", one_data)
            elif "delOrgRole" in one_data[1]:
                # 从ID列表中获取一条ID替换原ID
                one_test_data["id"] = id_list.pop(0)
            elif "deleteDir" in one_data[1]:
                one_test_data["dicCode"] = id_list.pop(0)
            dict2json = json.dumps(one_test_data, ensure_ascii=False)
            # 将修改后的数据插入到列表中
            one_data.insert(2, dict2json)
            # print("修改id后的数据：", one_data)
            restore_list.append(one_data)
        else:
            restore_list.append(one_data)
    return restore_list


# add_default_data = AddDefaultData()
# 通过接口插入初始的机构、角色、岗位、机构用户数据（声明为静态方法后，可以直接通过类名调用方法，不需要创建实例）
AddDefaultData.add_default_list_data(add_org_url, default_org_data_sheet_name)
AddDefaultData.add_default_dict_data(add_role_url, default_role_data_sheet_name)
AddDefaultData.add_default_list_data(add_position_url, default_position_data_sheet_name)
AddDefaultData.add_default_dict_data(add_user_url, default_user_data_sheet_name)

# 修改机构测试数据ID
org_code_list = ("GSB001", "GSB002", "GSB003", "GSB004", "GSB005", "GSB006", "GSB007", "GSB008", "GSB009")
org_test_data = change_test_data_id("hm_org", "org_code", org_code_list, "orgManage")
# print("机构测试数据：", org_test_data)

# 修改角色测试数据ID
role_name_list = ("T_业务经理", "T_权证跟单", "T_风控初审", "T_风控复审", "T_财务", "T_总经理")
role_test_data = change_test_data_id("hm_role", "role_name", role_name_list, "roleManage")
# print("角色测试数据：", role_test_data)

# 修改岗位测试数据ID
position_name_list = ("新增岗位1", "新增岗位2", "新增岗位3", "新增岗位4", "新增岗位5", "新增岗位6")
position_test_data = change_test_data_id("hm_dictionary_detail", "detail_value", position_name_list, "positionManage")
# print("岗位测试数据：", position_test_data)

# 修改机构用户测试数据ID
org_user_name_list = ("HMM01", "HMM02", "HMM03", "HMM04", "HMM05", "HMM06", "HMM07", "HMM08", "HMM09", "HMM10")
org_user_test_data = change_test_data_id("hm_user", "account", org_user_name_list, "orgUserManage")


# print("机构用户测试数据：", org_user_test_data)


# 获取订单详情
def get_order_bpmnInstId():
    sheet_name = "orderDetail"
    order_bpmnInstId = get_test_data(testDataFile, sheet_name)
    # print(order_bpmnInstId)
    return order_bpmnInstId


order_bpmnInstId = get_order_bpmnInstId()

# if __name__ == "__main__":
# add_default_org_user_info()
# add_default_position_info()
# change_org_user_test_info()
# get_order_bpmnInstId()
# add_default_role_info()
# change_org_test_info()

# # 删除机构、角色、岗位信息
# del_org_data()
# del_role_data()
# del_position_data()
# # 添加机构、角色、岗位信息
# add_default_org_info()
# add_default_role_info()
# add_default_position_info()
