import pymysql

conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="123456", db="testdb")
cursor = conn.cursor()


def queryData(id):
    querySQL = f"select * from tableName where id={id}"
    cursor.execute(querySQL)
    print("这是查询结果", cursor.fetchone())


def delData():
    delSql = "delete from tableName"
    try:
        cursor.execute(delSql)
        conn.commit()
    except:
        conn.rollback()
    finally:
        print("删除数据")


queryData(2)
