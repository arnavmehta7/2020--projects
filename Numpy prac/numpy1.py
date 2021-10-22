import numpy as np

# ~ arr = np.array([1, 2, 3, 4, 5])

# ~ print(arr)
# ~ print(type(arr))


# ~ arr = np.array([[1, 2, 3], [4, 5, 6]])

# ~ print(arr)


# ~ arr = np.array([1, 2, 3, 4], ndmin=5)  # define number of dimensions

# ~ print(arr)
# ~ print('number of dimensions :', arr.ndim)

# ~ arr = np.array([1,2,3,4])
# ~ print(arr.ndim)


# ~ arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

# ~ print('2nd element on 1st dim: ', arr[0][1])


def a(a,b):
	func = a*b
	print(func)
	
a(5,6)# no need of print as print is already in function


def myfunc(age,a):
	x = age*a
	print(x)
myfunc(3,7)

def rambo(n1,n2):
	return n1*n2
print(rambo(9,5))  # we neeed print heree
