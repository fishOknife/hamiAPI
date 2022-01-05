import pandas as pd
from getConfigInfo import *


# 获取指定列数据保存至列表中（数据驱动ddt）
def get_test_data(file_path, sheet_name):
    df = pd.read_excel(file_path, sheet_name, keep_default_na=False, usecols=[3, 4, 5, 6])
    list_test_data = df.values.tolist()
    return list_test_data


# 获取所有数据保存至列表中
def get_default_data(default_data_file_path, sheet_name):
    df = pd.read_excel(default_data_file_path, sheet_name, keep_default_na=False)
    list_default_data = df.values.tolist()
    return list_default_data[0]


# 获取所有列数据，组合为字典，再保存至列表中
def get_excel_data(file_path, sheet_name):
    df = pd.read_excel(file_path, sheet_name=sheet_name, keep_default_na=False)
    test_data = []
    # 获取表头
    keys = df.columns.values
    # 获取行号索引，并遍历
    for i in df.index.values:
        row_data = df.loc[i, keys].to_dict()
        test_data.append(row_data)
    return test_data


if __name__ == "__main__":
    sheetName = "Sheet1"
    testData = get_excel_data(defaultTestDataFile, sheetName)
    print(testData)
    # sheetName = "orgData"
    # testData = get_default_data(filePath, sheetName)
