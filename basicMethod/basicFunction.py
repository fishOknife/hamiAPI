import json
import requests
from basicMethod.basicInfo import *
from basicMethod.useMysql import query_id_from_table
from basicMethod.useExcel import get_excel_data, get_default_data, get_test_data


# 添加默认机构信息
def add_default_org_info():
    url = r"http://hami-test.tobowork.com:8026/stg/v1/system/org/addOrg"
    sheet_name = "orgData"
    # 从excel中获取数据
    one_org_info = get_excel_data(defaultDataFilePath, sheet_name)
    for i in range(0, len(one_org_info)):
        res = requests.post(url, headers=header, json=one_org_info[i])
        print("调接口插入机构信息：", res.text)


# 添加默认角色信息
def add_default_role_info():
    url = "http://hami-test.tobowork.com:8026/stg/v1/system/orgRole/addOrgRole"
    sheet_name = "roleData"
    # 从excel中获取数据
    one_org_info = get_default_data(defaultDataFilePath, sheet_name)
    for i in range(0, len(one_org_info)):
        json_data = json.loads(one_org_info[i])
        res = requests.post(url, headers=header, json=json_data)
        print("调接口插入角色信息：", res.text)


# 添加默认岗位信息
def add_default_position_info():
    url = "http://hami-test.tobowork.com:8026/stg/v1/system/dictionaryDetail/dicDetailAdd"
    sheet_name = "positionData"
    # 从excel中获取数据
    one_org_info = get_excel_data(defaultDataFilePath, sheet_name)
    for i in range(0, len(one_org_info)):
        res = requests.post(url, headers=header, json=one_org_info[i])
        print("调接口插入岗位信息：", res.text)


# 修改测试数据ID
def get_test_data_and_change_id(change_id_data, id_list, restore_list):
    for i in range(0, len(change_id_data)):
        one_data = change_id_data.pop(0)
        # 判断是否为编辑机构，因为编辑机构需要根据ID修改
        if "updateOrg" in one_data[1]:
            # print("修改id前的数据：", one_data)
            # 提取需要修改ID的数据，并转为dict
            one_test_data = eval(one_data.pop(2))
            # 从ID列表中获取一条ID替换原ID
            one_test_data["id"] = id_list.pop(0)
            # 将修改后的数据插入到列表中
            # print(type(one_test_data))
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


# 修改机构测试数据ID
def change_org_test_info():
    # 修改机构ID
    org_code_list = ("GSB001", "GSB002", "GSB003", "GSB004", "GSB005", "GSB006", "GSB007", "GSB008", "GSB009")
    # 从数据库中查询id,保存至列表中
    query_org_id_list = query_id_from_table("hm_org", "org_code", org_code_list)
    org_sheet_name = "orgManage"
    restore_org_list = []
    # 从excel中查询测试数据，保存至列表中
    all_org_data = get_test_data(testDataFilePath, org_sheet_name)
    changed_org_id_list = get_test_data_and_change_id(all_org_data, query_org_id_list, restore_org_list)
    # print("修改后的机构信息：", changed_org_id_list)
    return changed_org_id_list


def change_role_test_info():
    # 修改角色ID
    role_name_list = ("T_业务经理", "T_权证跟单", "T_风控初审", "T_风控复审", "T_财务", "T_总经理")
    # 从数据库中查询id,保存至列表中
    query_role_id_list = query_id_from_table("hm_role", "role_name", role_name_list)
    role_sheet_name = "roleManage"
    restore_role_list = []
    # 从excel中查询测试数据，保存至列表中
    all_role_data = get_test_data(testDataFilePath, role_sheet_name)
    changed_role_id_list = get_test_data_and_change_id(all_role_data, query_role_id_list, restore_role_list)
    # print("修改后的角色信息：", changed_role_id_list)
    return changed_role_id_list


def change_position_test_info():
    # 修改岗位ID
    detail_value_list = ("新增岗位1", "新增岗位2", "新增岗位3", "新增岗位4", "新增岗位5", "新增岗位6")
    # 从数据库中查询id,保存至列表中
    query_position_id_list = query_id_from_table("hm_dictionary_detail", "detail_value", detail_value_list)
    # print(query_position_id_list)
    position_sheet_name = "positionManage"
    restore_position_list = []
    # 从excel中查询测试数据，保存至列表中
    all_position_data = get_test_data(testDataFilePath, position_sheet_name)
    changed_position_id_list = get_test_data_and_change_id(all_position_data, query_position_id_list,
                                                           restore_position_list)
    # print("修改后的岗位信息：", changed_position_id_list)
    return changed_position_id_list


if __name__ == "__main__":
    change_org_test_info()
    # from basicMethod.useMysql import del_org_data, del_role_data, del_position_data
    #
    # # 删除机构、角色、岗位信息
    # del_org_data()
    # del_role_data()
    # del_position_data()
    # # 添加机构、角色、岗位信息
    # add_default_org_info()
    # add_default_role_info()
    # add_default_position_info()
