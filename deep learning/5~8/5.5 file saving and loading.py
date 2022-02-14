from mxnet import np, npx
from mxnet.gluon import nn

npx.set_np()

x = np.arange(4)
npx.save('x-file', x)

x2 = npx.load('x-file')
print(x2)

y = np.zeros(4)
npx.save('x-files', [x, y])
x2, y2 = npx.load('x-files')
print(x2, y2)


class MLP(nn.Block):
    def __init__(self, **kwargs):
        super(MLP, self).__init__(**kwargs)
        self.hidden = nn.Dense(256, activation='relu')
        self.output = nn.Dense(10)

    def forward(self, x):
        return self.output(self.hidden(x))


net = MLP()
net.initialize()
X = np.random.uniform(size=(2, 20))
Y = net(X)
print(net.collect_params())
net.save_parameters('mlp.params')

clone = MLP()
clone.load_parameters('mlp.params')

Y_clone = clone(X)
print(Y_clone == Y)
