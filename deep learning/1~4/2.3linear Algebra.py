from mxnet import np, npx

npx.set_np()

# x = np.array(3.0)
# y = np.array(2.0)
#
# print(x + y, x * y, x / y, x ** y)
#
x = np.arange(4)
# print(x)
#
# print(x[3])
#
print(len(x))
# print(x.shape)
#
# A = np.arange(20).reshape(5, 4)
# print(A)
#
# print(A[1, 2])
#
# print(A.T)
#
# B = np.array([[1, 2, 3], [2, 0, 4], [3, 4, 5]])
#
# print(B)
# print(B == B.T)

# X = np.arange(24).reshape(2, 3, 4)
# print(X)

A = np.arange(20).reshape(5, 4)
B = A.copy()  # Assign a copy of `A` to `B` by allocating new memory
# print(A, A + B)

# print(A * B)

a = 2
X = np.arange(24).reshape(2, 3, 4)
# print(a + X, (a * X).shape)
#
# print(A.sum())
#
# A_sum_axis0 = A.sum(axis=0)
#
# print(A_sum_axis0, A_sum_axis0.shape)
#
# A_sum_axis1 = A.sum(axis=1)
# print(A_sum_axis1, A_sum_axis1.shape)
#
# print(A.sum(axis=[0, 1]))  # Same as `A.sum()`
#
# print(A.mean(), A.sum() / A.size)
#
# print(A.mean(axis=0), A.sum(axis=0) / A.shape[0])
#
# sum_A = A.sum(axis=1, keepdims=True)
# print(sum_A)
#
# print(A / sum_A)
#
# print(A.cumsum(axis=0))
#
# y = np.ones(4)
# print(x, y, np.dot(x, y))
# print((x * y).sum())

print(x)
print(A)
print(A.shape)
print(x.shape)
print(np.dot(A, x))
print((np.dot(A, x)).shape)

u = np.array([3, -4])
print(np.linalg.norm(u))
print(np.abs(u).sum())
print(np.linalg.norm(np.ones((4, 9))))
