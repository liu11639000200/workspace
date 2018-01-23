from pymysql import  *


def create():
    # 创建Connection连接
    conn = connect(host='localhost',port=3306,database='stock_db',user='root',password='mysql',charset='utf8')
    # 获得Cursor对象
    cs1 = conn.cursor()

    # 创建表
    create_sql = """ CREATE TABLE IF NOT EXISTS user(uid int unsigned,name varchar(30),email varchar(30),password varchar(30));"""
    cs1.execute(create_sql)

    # 提交
    conn.commit()

    # 关闭
    cs1.close()
    conn.close()

def insert(**kwargs):

    print(kwargs)
    # 创建Connection连接
    conn = connect(host='localhost', port=3306, database='stock_db', user='root', password='mysql', charset='utf8')
    # 获得Cursor对象
    cs1 = conn.cursor()

    # 插入数据
    insert_sql = """ insert into user (uid,name,email,password) values (123,'oldyang','test@orm.org','pwd');"""
    cs1.execute(insert_sql)

    # 提交
    conn.commit()

    # 关闭
    cs1.close()
    conn.close()

def main():
    create()
    insert(uid = 123,name = "old样",email = "test@orm.org",password = "pwd")


if __name__ == '__main__':
    main()