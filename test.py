a = [1,2,3,4,5]
b = []

b = map(lambda x: x*x, a)

print(list(b))


class Test():
	def __bool__(self):
		print('bool')
		return True
	def __len__(self):
		print('len')
		return 0

print(bool(Test()))

print("------------------")
assert 1==1
print('?')

print("------------------")
def test(m):
	a=m
	print(a)

test(10)
