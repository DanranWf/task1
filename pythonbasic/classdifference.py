# class A():
#     def __init__(self):
#         pass
#     def save(self):
#         print( "This is from A")
# class B(A):
#     def __init__(self):
#         pass
# class C(A):
#     def __init__(self):
#         pass
#     def save(self):
#         print( "This is from C")
# class D(B,C):
#     def __init__(self):
#         pass
# fun =  D()
# fun.save()

# classical-py2.X This is from A
# newclass-py3.X  This is from C

class A():
     def add(self, x):
         y = x+1
         print(y)
         return y
class B(A):
    def cc(self, x):
        super(B,self).add(x)


class C(B):
    def lwj(self,x):
        ee=A().add(x)
        print(ee)
        return ee


b = B()
b.cc(2)  # 3
b.add(5)

print('11111111',C().lwj(3))
print(type(b))
print(b.__class__)



