import requests
import base64
import json
import pandas as pd
import configparser
import pymysql


# 创建数据库链接
def connMysql():
    conf = configparser.ConfigParser()
    conf.read("config.ini", encoding="utf-8")
    host = conf.get("mysql", "host")
    port = conf.getint("mysql", "port")
    user = conf.get("mysql", "user")
    pw = conf.get("mysql", "password")
    db = "hami_db_stg"
    print(host)
    conn = pymysql.connect(host=host, port=port, user=user, password=pw, db=db)
    cursor = conn.cursor()
    return conn, cursor

connMysql()

# conf = configparser.ConfigParser()
# conf.read("config.ini", encoding="utf-8")
# headers = dict(conf.items("header"))
# print(headers)


# 获取消息通知
def getWarnNotice(id):
    getWarnNoticeURL = "http://hami-test.tobowork.com:8026/stg/v1/bussiness/warn/queryWarnNotice"
    params = {
        "id": id
    }
    res = requests.get(url=getWarnNoticeURL, headers=header, params=params)
    print(res.request.url)
    return res.text


# warnNoteice = getWarnNotice("10000001270859")
# print("获取消息通知：",warnNoteice)

# ================机构================
# 获取全部机构信息
def getAllOrgInfo():
    getOrgURL = "http://hami-test.tobowork.com:8026/stg/v1/system/org/pageOrg"
    data = {}
    res = requests.post(url=getOrgURL, headers=header, json=data)
    return res.text


# orgInfo = getAllOrgInfo()
# print("机构信息：",orgInfo)

# 新增机构
def addOneOrg():
    addOneOrgURL = "http://hami-test.tobowork.com:8026/stg/v1/system/org/addOrg"
    filePath = r"C:\Users\admin\Desktop\哈密\HMAPITest\testData\testData.xlsx"
    sheetName = "addOrgInfo"
    df = pd.read_excel(filePath, sheetName, keep_default_na=False, usecols=[4, 5])
    list_data = df.values.tolist()
    data = list_data[0][0]
    jsonData = json.loads(data)
    print(type(data))
    res = requests.post(url=addOneOrgURL, headers=header, json=jsonData)
    return res.text


# addOneOrgResult = addOneOrg()
# print(addOneOrgResult)

# 编辑机构(根据ID修改机构信息)
def updateOrgInfo():
    updateOrgURL = "http://hami-test.tobowork.com:8026/stg/v1/system/org/updateOrg"
    data = {
        "id": 13,
        "orgCode": "HM01003",
        "orgName": "吐鲁番2分局",
        # "parentOrgId": "",
        # "discription": "",
        # "type": 1
    }
    res = requests.post(url=updateOrgURL, headers=header, json=data)
    return res.text


# updateOrgResult=updateOrgInfo()
# print("更新机构返回结果：",updateOrgResult)

# 删除机构（业务系统已删除，工作流未删除）
def delOrgInfo(orgID):
    delOrgURL = "http://hami-test.tobowork.com:8026/stg/v1/system/org/deleteOrg"
    # 机构id75为“西北研究院”
    params = {"orgId": orgID}
    res = requests.get(url=delOrgURL, headers=header, params=params)
    print(res.request.url)
    return res.text


# deleteOrgResult = delOrgInfo(20)
# print("删除机构返回结果：",deleteOrgResult)

# ================岗位================
# 获取订单节点信息
def getNodeInfo():
    getNodeInfoURL = "http://hami-test.tobowork.com:8026/stg/v1/bussiness/workflow/processHandle/getVerifyHistoryByFlowId"
    params = {"bpmnInstId": "10000003920283"}
    res = requests.post(url=getNodeInfoURL, headers=header, params=params)
    print(res.text)
    return res.text


# nodeInfo = getNodeInfo()
# print("订单节点信息：",nodeInfo)

# 获取字典信息
def getDirInfo():
    getDirURL = "http://hami-test.tobowork.com:8026/api/v1/system/tbflow/tbflow/dic/getByDicType"
    res = requests.get(getDirURL, header)
    print(res.text)
    return res.text


# dirInfo = getDirInfo()
# print(dirInfo)

# 获取代办列表
def getPindingMatters():
    pendingMattersURL = "http://hami-test.tobowork.com:8026/api/v1/tbflow/tbflow/receivedProcess/pendingJson"
    res = requests.get(url=pendingMattersURL, headers=header)
    print(res.request.url)
    print(res.text)
    return res.text


# pingingMatters = getPindingMatters()
# print(pingingMatters)

# 身份证识别
def ocrIdentity():
    OCRIDCardURL = "http://hami-test.tobowork.com:8026/api/v1/hub/tripartite/ocrIdentity"

    # 将图片转为base64格式
    with open(r'C:\Users\admin\Desktop\哈密\测试附件\IDCard1.jpg', 'rb') as f:
        base64_data = base64.b64encode(f.read())
        s = base64_data.decode()

    # 将数据组合为字典
    data = {
        "base64Content": s,
        "type": "0"
    }

    res = requests.post(url=OCRIDCardURL, headers=header, json=data)

    return res.text


# ocrInfo = ocrIdentity()
# print(ocrInfo)

# 添加用户，添加机构、渠道用户（type传1、2）报错：服务器内部错误
def addUserInfo():
    addUserURL = "http://hami-test.tobowork.com:8026/stg/v1/system/user/addUser"
    userInfo = {
        "userName": "权证跟单",
        "account": "hm01003",
        "password": "123456",
        "telephone": "13100000003",
        "orgCode": "HM01",
        "orgId": 1,
        "type": 3,
        "status": "1"
    }

    res = requests.post(url=addUserURL, headers=header, json=userInfo)

    return res.text


# userInfo = addUserInfo()
# print(userInfo)

# login_data = {
#     "account": "admin",
#     "password": "21232f297a57a5a743894a0e4a801fc3",
#     "codeKey": "b307fff8-21c4-4db0-aec0-b4d9d7a9c8a0",
#     "verifyCode": "ylsi",
#     "systemFlag": "pc"
# }
#
# res = requests.post(url="http://hami-test.tobowork.com:8026/stg/v1/system/user/login", headers=header,
#                     json=login_data)
# print(res.text)

# 获取订单详情（bpmnInstId为工作流的bpm_pro_inst的BPMN_INST_ID_字段）
def get_order_detail():
    get_order_detail_url = "http://hami-test.tobowork.com:8026/stg/v1/bussiness/workflow/processHandle/getFormAndData"
    data = {
        "bpmnInstId": "10000003920283"
    }
    res = requests.post(url=get_order_detail_url, headers=header, json=data)
    print("订单详情：", res.text)

# get_order_detail()
