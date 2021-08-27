import pandas as pd


# 将excel中的数据组合为字典形式，保存在列表中
def getExcelData(filePath, sheetName):
    df = pd.read_excel(filePath, sheet_name=sheetName, keep_default_na=False)
    test_data = []
    # 获取表头
    keys = df.columns.values
    # 获取行号索引，并遍历
    for i in df.index.values:
        row_data = df.loc[i, keys].to_dict()
        test_data.append(row_data)
    return test_data


if __name__ == "__main__":
    filePath = r"F:\Python38\APITestModel\testData\testData.xlsx"
    sheetName = "登录"
    testData = getExcelData(filePath, sheetName)
    print(testData)
    # 将字符串转为字典
    # str2dict = eval(testData[0]['requestData'])
    # print(str2dict["phone"])
