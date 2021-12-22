import pymysql
import random

conn = pymysql.connect(host="of.tobosoft.com.cn", port=8032, user="hami", password="kWS8^yg4bYNAP86x", db="hami_db_stg")
cursor = conn.cursor()


# 查询表中所有的信息
def query_info(table_name):
    query_sql = f"select * from {table_name}"
    cursor.execute(query_sql)
    # print("这是查询结果", cursor.fetchall())
    fetch_result = cursor.fetchall()
    return fetch_result


def del_data(table_name):
    del_sql = f"delete from {table_name}"
    try:
        cursor.execute(del_sql)
        conn.commit()
        print("删除成功")
    except:
        conn.rollback()
        print("删除失败，回滚")


queryResult = query_info("hm_org")
print(queryResult)
# oneData = random.randint(0, len(queryResult) - 1)
# print(queryResult[oneData][0])
