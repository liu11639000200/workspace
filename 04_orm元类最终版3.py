from pymysql import  *

class Field(object):
    def __init__(self,data):
        self.data = data

class MyMetaClass(type):

    def __new__(cls, class_name,supers_name,attrs):
        print(attrs)

        create_dict = dict() # 创建我们字段的字典
        for key,value in attrs.items():
            if isinstance(value,Field): # 我们要的是元组数据
                create_dict[key] = value.data

        attrs['create_dict']  = create_dict # 自动生成一个属性的字典

        attrs['table_name'] = class_name.lower()

        # 删除以前自己写的字段
        for key in create_dict.keys():
            print(key)
            attrs.pop(key)



        return type.__new__(cls,class_name,supers_name,attrs)


class Table(object,metaclass=MyMetaClass):



    # dicts = {"uid":uid,"name":name,"email":email,"password":password}


    def create(self):

        # create_dict = {"uid":"int unsigned","name":"varchar(30)","email":"varchar(30)","password":"varchar(30)"}

        # 创建Connection连接
        conn = connect(host='localhost',port=3306,database='stock_db',user='root',password='mysql',charset='utf8')
        # 获得Cursor对象
        cs1 = conn.cursor()

        fields = list()

        for key,value in self.create_dict.items():
            fields.append("%s %s"%(key,value))


        print(self.create_dict)

        # 创建表
        # create_sql = """ CREATE TABLE IF NOT EXISTS user(uid int unsigned,name varchar(30),email varchar(30),password varchar(30));"""
        create_sql = """ CREATE TABLE IF NOT EXISTS %s(%s);"""%(self.table_name,",".join(fields),)

        print(create_sql)


        cs1.execute(create_sql)

        # 提交
        conn.commit()

        # 关闭
        cs1.close()
        conn.close()

    def insert(self,**kwargs):

        print(kwargs)
        # 创建Connection连接
        conn = connect(host='localhost', port=3306, database='stock_db', user='root', password='mysql', charset='utf8')
        # 获得Cursor对象
        cs1 = conn.cursor()

        # 插入数据
        # insert_sql = """ insert into user (uid,name,email,password) values (123,'oldyang','test@orm.org','pwd');"""
        keys = list()
        values = list()

        for key,value in kwargs.items():
            keys.append(key)
            # 如果是Int转成字符串
            if isinstance(value , int):
                # 说明 int
                values.append(str(value))
            else:
                values.append(""" "%s" """%value)


        insert_sql = """ insert into %s (%s) values (%s);"""%(self.table_name,",".join(keys),",".join(values))

        print(insert_sql)

        cs1.execute(insert_sql)

        # 提交
        conn.commit()

        # 关闭
        cs1.close()
        conn.close()

def set_args(data):

    def set_fun(func):
        def call_fun(*args,**kwargs):
            return func(*args,**kwargs)
        return call_fun
    return set_fun


@set_args(123)
class LowUser(Table):
    name = Field("varchar(20)")
    password = Field("varchar(20)")

class Login(Table):
    name = Field("varchar(20)")




# class Login(Table):
#
#     name = ("varchar(20)",)
#     password = ("varchar(20)",)
#     address = ("varchar(20)",)

def main():
    lowUser = LowUser()
    lowUser.create()
    lowUser.insert(name = "old样",password = "654321")

    login = Login()
    login.create()
    login.insert(name = "898989")

    print(Login.name)

    # login = Login()
    # login.create()
    # login.insert(name = "yy",password = 'xyy' ,address = "上海传智old样")




    # create()
    # # insert(uid = 123,name = "old样",email = "test@orm.org",password = "pwd")
    # insert(uid = 123)
    #
    # # """insert into user (password,email,name,uid) values ("pwd","test@orm.org","old样",123);"""
    #


if __name__ == '__main__':
    main()