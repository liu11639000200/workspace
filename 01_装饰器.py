
def set_fun(func):
    print("func%s"%str(func))

    def call_fun(*args,**kwargs):
        return func(*args,**kwargs)

    print("call_fun%s"%call_fun)
    return call_fun

@set_fun
def test():
    print("test is show")

test()

print("test is%s"%test)

# 13行的test(test()) 是set_fun下的call_fun
# 2行的参数func是第八行(def set_fun(func):)




