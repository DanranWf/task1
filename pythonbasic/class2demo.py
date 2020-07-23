class A(object):
	"""docstring for A"""
	def __init__(self, arg):
		super().__init__()
		self.arg = arg
	def add(self):
		return self.arg+1

aa=A(3)
print('A new instance and with arg 3',aa)
print('called A.add()mehod',aa.add())

#================================

class B:
	"""docstring for ClassName"""
	def __init__(self, arg):
		super(B, self).__init__()
		self.arg = arg
print('B new instance and with arg 5',B(5))

#================================

class C(object):
	"""docstring for C"""
	def __init__(self, arg):
		super(C, self).__init__()
		self.arg = arg

#================================

class A:
	def foo(self):
		print('called A','called A.foo()')

class B(A):
	pass

class C(A):
	def foo(self):
		print('called C','called C.foo()')

class D(B, C):
	pass


d = D()
d.foo()


		