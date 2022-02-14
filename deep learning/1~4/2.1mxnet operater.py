from mxnet import np, npx

npx.set_np()
# x = np.arange(12)
# print(x)
# print(x.shape)
# print(x.size)
# X = x.reshape(3, 4)
# print(X)
# print(np.zeros((2, 3, 4)))
# print(np.ones((2, 3, 4)))
# print(np.random.normal(0, 1, size=(3, 4)))
# print(np.array([[2, 1, 4, 3], [1, 2, 3, 4], [4, 3, 2, 1]]))

x = np.array([1, 2, 4, 8])
y = np.array([2, 2, 2, 2])
print(x + y, x - y, x * y, x / y, x ** y)
print(np.exp(x))
print(id(y))
