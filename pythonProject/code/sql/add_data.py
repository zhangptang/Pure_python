# -*-coding:utf-8-*-
import pymysql

no = int(input('部门编号: '))
name = input('部门名称: ')
location = input('部门所在地: ')

# 创建连接
conn = pymysql.connect(host='sql6.freemysqlhosting.net', port=3306,
                       user='sql6501453', database='sql6501453', password='cxJuD163DR',
                       charset='utf8mb4', autocommit=True)

try:
    # 获取游标对象
    with conn.cursor() as cursor:
        affected_rows = cursor.execute(
            'insert into `tb_dept` values (%s, %s, %s)',
            (no, name, location)
        )
        if affected_rows == 1:
            print('add dept success!')
finally:
    conn.close()
