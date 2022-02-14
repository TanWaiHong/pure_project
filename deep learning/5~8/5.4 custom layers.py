from mxnet import np, npx
from mxnet.gluon import nn

npx.set_np()

class CenteredLayer(nn.Block):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def forward(self, X):
        return X - X.mean()


layer = CenteredLayer()
layer(np.array([1, 2, 3, 4, 5]))

net = nn.Sequential()
net.add(nn.Dense(128), CenteredLayer())
net.initialize()

Y = net(np.random.uniform(size=(4, 8)))
print(Y.mean())
print(net.collect_params())


class MyDense(nn.Block):
    def __init__(self, units, in_units, **kwargs):
        super().__init__(**kwargs)
        self.weight = self.params.get('weight', shape=(in_units, units))
        self.bias = self.params.get('bias', shape=(units,))

    def forward(self, x):
        linear = np.dot(x, self.weight.data(ctx=x.ctx)) + self.bias.data(
            ctx=x.ctx)
        return npx.relu(linear)


net = nn.Sequential()
net.add(MyDense(8, in_units=64),
        MyDense(1, in_units=8))
net.initialize()
print(net(np.random.uniform(size=(2, 64))))
print(net.collect_params())
