def func1(a):
	print(1)
	print(a)


def func2(b):
	print(2) 
	print(b)


def func3():
	print(3)


def func4():
	print(4)


lx = (func1, func2)
ly = (func3(), func4())

for i in lx:
	i(15)
print("LOL")
for i in ly:
	i
