class A(object):
	"""docstring for A"""
	def __init__(self, arg):
		super().__init__()
		self.arg = arg
	def add(self):
		return self.arg+1

aa=A(3)
print(aa)
print(aa.add())

class B:
	"""docstring for ClassName"""
	def __init__(self, arg):
		super(B, self).__init__()
		self.arg = arg
print(B(5))


class C(object):
	"""docstring for C"""
	def __init__(self, arg):
		super(C, self).__init__()
		self.arg = arg

class A:
def foo(self):
print(‘called A.foo()’)

class B(A):
pass

class C(A):
def foo(self):
print(‘called C.foo()’)

class D(B, C):
pass

if name == ‘main’:
d = D()
d.foo()


		