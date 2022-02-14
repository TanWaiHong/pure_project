from mxnet import autograd, np, npx

npx.set_np()

x = np.arange(4.0)
print(x)

# We allocate memory for a tensor's gradient by invoking `attach_grad`
x.attach_grad()
# After we calculate a gradient taken with respect to `x`, we will be able to
# access it via the `grad` attribute, whose values are initialized with 0s
print(x.grad)

# Place our code inside an `autograd.record` scope to build the computational
# graph
with autograd.record():
    y = 2 * np.dot(x, x)
print(y)

y.backward()
print(x.grad)

print(x.grad == 4 * x)

with autograd.record():
    y = x.sum()
y.backward()
print(x.grad)  # Overwritten by the newly calculated gradient

# When we invoke `backward` on a vector-valued variable `y` (function of `x`),
# a new scalar variable is created by summing the elements in `y`. Then the
# gradient of that scalar variable with respect to `x` is computed
with autograd.record():
    y = x * x  # `y` is a vector
y.backward()
print(y)
print(x.grad)  # Equals to y = sum(x * x)

with autograd.record():
    y = x * x
    u = y.detach()
    z = u * x
z.backward()
print(u)
print(x.grad == u)


def f(a):
    b = a * 2
    while np.linalg.norm(b) < 1000:
        b = b * 2
    if b.sum() > 0:
        c = b
    else:
        c = 100 * b
    return c


a = np.random.normal()
print(a)
a.attach_grad()
with autograd.record():
    d = f(a)
d.backward()

print(a.grad == d / a)

from d2l import mxnet
import matplotlib.pyplot as plt

x = np.linspace(-5, 6)
x.attach_grad()
with autograd.record():
    y = np.sin(x)

y.backward()

mxnet.plot(x, (y, x.grad), legend=['sin(x)', 'grad x'])
plt.show()
