class CC(object):
    num = 100

    def test(self):
        print("test is show")

cc = CC()
cc.test()

xx = CC
bb = xx()
bb.test()

a = 100

# print(type(a))

# print(help(int))

print(cc.__class__)
print(cc.__class__.__class__)
print(cc.__class__.__class__.__class__)

print(int.__class__)

