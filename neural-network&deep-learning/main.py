import mnist_loader
import network
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

training_data, validation_data, test_data = mnist_loader.load_data_wrapper()

net = network.Network([784, 30, 10])
net.SGD(training_data, 30, 10, 3, test_data=test_data)

is_go = True
while is_go:
    if input("checking?(yes/no): ") == "yes":
        is_go = True
    else:
        is_go = False
    if is_go:
        im_frame = Image.open('pixil-frame-0.png').convert('L')
        plt.imshow(np.reshape(im_frame, (28, 28)) / 255, cmap=plt.get_cmap('gray'))
        plt.show()
        im_frame = np.reshape(im_frame, (784, 1)) / 255
        print(np.argmax(net.feedforward(im_frame)))
