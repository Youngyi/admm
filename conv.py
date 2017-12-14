import numpy as np
from scipy import signal
from sklearn.datasets import load_digits

digits = load_digits()


a = digits.data[0].reshape((8,8))
k = np.array([[1,2],[3,4]])

#x = np.array([[a[0,0], a[0,1], a[1,0], a[1,1]], [a[0,1], a[0,2], a[1,1], a[1,2]], [a[1,0], a[1,1], a[2,0], a[2,1]], [a[1,1], a[1,2], a[2,1], a[2,2]]])

# print(x_dash)

y = signal.convolve2d(a, np.rot90(k, 2), 'valid')
print(y)
def convert_conv(im, k):
	'''x, is the input image, k is the kernel size'''
	y, x = im.shape
	toeplitz = np.zeros(((y - k + 1) * (y - k + 1), k * k))
	y_ = y - k + 1
	x_ = x - k + 1
	count = 0
	for i in range(y_):
		for j in range(x_):
			toeplitz[count, :] = im[i:i+k, j:j+k].reshape((k*k))
			count += 1
	return toeplitz

p = convert_conv(a, 2)
print(np.dot(np.linalg.pinv(p), y.reshape((p.shape[0])) ))
