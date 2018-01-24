# 动态生成一个字典
import re
url_dict = dict()

url_dict2 = dict()

# 三层嵌套,第三层返回第二层闭包的对象引用,必须第三层都有参数
def set_args(data):
    def set_fun(func):


        def call_fun(*args, **kwargs):
            return func(*args, **kwargs)

        url_dict2[data] = call_fun

        return call_fun

    return set_fun


@set_args('/add/123.html')  # xxxx(123)先执行,执行完返回肯定是一个闭包, 第二步@闭包
def test():
    print("test1 is show")

@set_args('/add/456.html')  # xxxx(123)先执行,执行完返回肯定是一个闭包, 第二步@闭包
def test():
    print("test 2is show")

@set_args(r"/add/(\d+).html")
def add_method():
    print("add")


# /add/9999.html

for re_str,method in url_dict2.items():
    match = re.match(re_str, "/add/0980980.html")
    if match:
        # 说明有数据
        print('匹配了')
        method()
        print(match.group(1))
