# @Time : 2023/9/29 7:35
# @Author : 雷洋平
# @File : operational_database.py
# @Software: PyCharm
# @Function: 操作数据库
import pymysql


class DoMySQL:
    def __init__(self, user="root", pwd="root", host="127.0.0.1", db="woniusales", port: int = 3306, charset="utf8"):
        # 创建数据库链接、游标
        self.con = pymysql.connect(user=user, password=pwd, host=host, database=db, port=port, charset=charset)
        self.cur = self.con.cursor()

    # SQL查询语句
    def query_sql(self, sql, flag="all", size: int = 0):
        # 预执行sql语句
        self.cur.execute(sql)
        if flag == "one":
            rest = self.cur.fetchone()
        if flag == "many":
            rest = self.cur.fetchmany(size)
        if flag == "one":
            rest = self.cur.fetchall()
        return rest

    def modify_sql(self, sql):
        # sql预执行
        self.cur.execute(sql)
        # 提交事务
        self.con.commit()

    # 执行析构方法，对象被销毁时自动调用的方法：断开链接
    def __del__(self):
        self.cur.close()
        self.con.close()


if __name__ == '__main__':
    pass
    sql_db = DoMySQL()
    sql = f"update `store` set `createtime` = '2023-09-26 18:28:46'where goodsid = '307';"
    sql_db.modify_sql(sql)
