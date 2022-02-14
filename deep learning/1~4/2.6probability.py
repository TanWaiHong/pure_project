import random
from mxnet import np, npx
from d2l import mxnet as d2l

npx.set_np()

fair_probs = [0.5, 0.5]
x = np.random.multinomial(1, fair_probs)
print(x)

print(np.random.multinomial(1000, fair_probs))

for help in range(2):
    print(help)
