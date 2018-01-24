# 动态生成一个字典

url_dict = dict()

url_dict2 = dict()

# 三层嵌套,第三层返回第二层闭包的对象引用,必须第三层都有参数
def set_args(data):
    def set_fun(func):
        print("func%s" % str(func))

        url_dict[data] = func

        def call_fun(*args, **kwargs):
            print("show")
            return func(*args, **kwargs)

        url_dict2[data] = call_fun

        print("call_fun%s" % str(call_fun))
        return call_fun

    return set_fun


@set_args('123')  # xxxx(123)先执行,执行完返回肯定是一个闭包, 第二步@闭包
def test():
    print("test is show")


print(test)

print(url_dict)
print(url_dict2)

url_dict['123']()
print("-"*90)
url_dict2['123']()
