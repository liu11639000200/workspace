# class CC(object):

# type("类名",(父类1,父类2),{属性:值})

class A(object):
    num = 100


B = type("B", (object,), {"num": 300})


# print(help(A))
# print(help(B))

print(A.num)
print(B.num)
