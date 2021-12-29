import pymysql


def connect_mysql(db):
    conn = pymysql.connect(host="of.tobosoft.com.cn", port=8032, user="hami", password="kWS8^yg4bYNAP86x", db=db)
    cursor = conn.cursor()
    return conn, cursor


# 查询表中所有的信息
def query_info(table_name):
    conn, cursor = connect_mysql("hami_db_stg")
    query_sql = f"select * from {table_name}"
    cursor.execute(query_sql)
    # print("这是查询结果", cursor.fetchall())
    fetch_result = cursor.fetchall()
    return fetch_result


# 传入表名、字段名、值，查询ID,返回list
def query_id_from_table(table_name, field_name, values):
    id_list = []
    conn, cursor = connect_mysql("hami_db_stg")
    query_sql = f"select id from {table_name} where {field_name} in %s" % (values,)
    cursor.execute(query_sql)
    fetch_result = cursor.fetchall()
    for i in range(0, len(fetch_result)):
        id_list.append(fetch_result[i][0])
    return id_list


# 删除业务系统、工作流机构信息
def del_org_data():
    # 删除业务系统信息
    conn, cursor = connect_mysql("hami_db_stg")
    del_org_sql = "delete from hm_org where id >=41"

    try:
        cursor.execute(del_org_sql)
        conn.commit()
        print("删除业务系统机构信息成功")
    except:
        conn.rollback()
        print("删除业务系统机构信息失败，回滚")
    finally:
        conn.close()
        cursor.close()
        print("关闭业务系统数据库链接")

    # 删除工作流信息
    conn, cursor = connect_mysql("hami_workflow_stg")
    del_sys_org_sql = "delete from sys_org where CODE_ >=41"
    try:
        cursor.execute(del_sys_org_sql)
        conn.commit()
        print("删除工作流机构信息成功")
    except:
        conn.rollback()
        print("删除工作流机构信息失败，回滚")
    finally:
        conn.close()
        cursor.close()
        print("关闭工作流数据库链接")


# 删除业务系统角色信息，角色菜单权限（角色信息未同步工作流，）
def del_role_data():
    conn, cursor = connect_mysql("hami_db_stg")
    del_role_sql = "delete from hm_role where id >=146"
    del_role_menu_sql = "delete from hm_role_menu where role_id >=146"
    try:
        cursor.execute(del_role_sql)
        cursor.execute(del_role_menu_sql)
        conn.commit()
        print("删除角色信息成功")
    except:
        conn.rollback()
        print("删除角色信息失败，回滚")
    finally:
        conn.close()
        cursor.close()
        print("关闭业务系统数据库链接")


# 删除岗位信息（业务系统、工作流）
def del_position_data():
    # 删除业务系统岗位信息
    conn, cursor = connect_mysql("hami_db_stg")
    del_position_sql = "delete from hm_dictionary_detail where dic_id=4 and id>=294"
    try:
        cursor.execute(del_position_sql)
        conn.commit()
        print("删除业务系统岗位信息成功")
    except:
        conn.rollback()
        print("删除业务系统岗位信息失败，回滚")
    finally:
        conn.close()
        cursor.close()
        print("关闭业务系统数据库链接")

    # 删除业务系统岗位信息
    conn, cursor = connect_mysql("hami_workflow_stg")
    del_position_sql = "delete from sys_org_rel where ID_>=10000003770727"
    try:
        cursor.execute(del_position_sql)
        conn.commit()
        print("删除工作流岗位信息成功")
    except:
        conn.rollback()
        print("删除工作流岗位信息失败，回滚")
    finally:
        conn.close()
        cursor.close()
        print("关闭工作流数据库链接")


if __name__ == "__main__":
    query_org_code = ("GSB001", "GSB002", "GSB003", "GSB004", "GSB005", "GSB006", "GSB007", "GSB008", "GSB009")
    queryResult = query_id_from_table("hm_org", "org_code", query_org_code)
    print(queryResult)
    # del_org_data()
