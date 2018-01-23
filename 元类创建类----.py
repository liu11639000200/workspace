class AA(object):
    num=1000


print(AA.num)


AA= type('AA',(object,),{'num':1000})
print(AA.num)