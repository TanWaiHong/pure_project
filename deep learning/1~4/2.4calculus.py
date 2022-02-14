from mxnet import np, npx
from d2l import mxnet as d2l
import matplotlib.pyplot as plt

npx.set_np()


def f(x_long):
    return 3 * x_long ** 2 - 4 * x_long


def numerical_lim(f_, x_long, high):
    return (f_(x_long + high) - f_(x_long)) / high


h = 0.1
for i in range(5):
    print(f'h={h:.5f}, numerical limit={numerical_lim(f, 1, h):.5f}')
    h *= 0.1

x = np.arange(0, 3, 0.1)

d2l.plot(x, [f(x), 2 * x - 3], 'x', 'f(x)', legend=['f(x)', 'Tangent line (x=1)'])
plt.show()
