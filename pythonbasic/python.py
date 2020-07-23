# demo1   
def lwj():
    a=0
    if a<1:
        print(a)
        a=a+1
    return a>=1      #========= return value is a Bool


print(lwj())
# print(lwj().a)  #========= AttributeError: 'bool' object has no attribute 'a'

#demo2
class A:
    def fx(self):
        pass

xa = A()
xb = A()
if xa == xb:
    print("==")     #=========== class instance cannot be compared,only attribute can compare
else:
	print('!=')


#demo3   #============
token='234jk324ka7a9'
b="token {}".format(token)
print(b)


class A(object):
	"""docstring for A"""
	def __init__(self, arg):
		super(A, self).__init__()
		self.arg = arg

class ClassName(object):
	"""docstring for ClassName"""
	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg


		
		