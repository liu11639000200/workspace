# class CC(object):

# type("类名",(父类1,父类2),{属性:值})

class A(object):
    num = 100

    @classmethod
    def test(cls):
        print("test is show")

@classmethod
def test(cls):
    print("test type is show")

B = type("B", (object,), {"num": 100,"test":test})

#
# print(help(A))
# print(help(B))
#
A.test()
B.test()

