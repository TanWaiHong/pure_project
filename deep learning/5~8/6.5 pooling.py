from mxnet import np, npx
from mxnet.gluon import nn
from d2l import mxnet as d2l

npx.set_np()


def pool2d(X, pool_size, mode='max'):
    p_h, p_w = pool_size
    Y = np.zeros((X.shape[0] - p_h + 1, X.shape[1] - p_w + 1))
    for i in range(Y.shape[0]):
        for j in range(Y.shape[1]):
            if mode == 'max':
                Y[i, j] = X[i: i + p_h, j: j + p_w].max()
            elif mode == 'avg':
                Y[i, j] = X[i: i + p_h, j: j + p_w].mean()
    return Y


X = np.array([[0.0, 1.0, 2.0], [3.0, 4.0, 5.0], [6.0, 7.0, 8.0]])
print(pool2d(X, (2, 2)))
print(pool2d(X, (2, 2), 'avg'))

X = np.arange(16, dtype=np.float32).reshape((1, 1, 4, 4))
print(X)

pool2d = nn.MaxPool2D(3)
# Because there are no model parameters in the pooling layer, we do not need
# to call the parameter initialization function
print(pool2d(X))

pool2d = nn.MaxPool2D(3, padding=1, strides=2)
print(pool2d(X))

pool2d = nn.MaxPool2D((2, 3), padding=(0, 1), strides=(2, 3))
print(pool2d(X))

X = np.concatenate((X, X + 1), 1)
print(X)

pool2d = nn.MaxPool2D(3, padding=1, strides=2)
print(pool2d(X))
