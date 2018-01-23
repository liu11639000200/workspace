def changeClass(class_name,supers_name,attrs):
    print("changattrs")

    attrs['num'] = 0

    attrs['lele'] = "i love you!"

    return type(class_name,supers_name,attrs)

class AA(object,metaclass=changeClass):

    num = 100


aa = AA()

print(aa.lele)
print(AA.lele)