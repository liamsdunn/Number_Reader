import random
import numpy as np


class Network():

	# Intilizes the number of layers, the # of nodes in each layer,
	# and randomly inititalizes the weights and biases.
	def __init__(self,sizes):
		self.num_of_layers = sizes
		self.layer_sizes = sizes
		self.biases = [np.random.randn(y,1) for y in sizes[1:]]
		self.weights = [np.random.randn(x,y) for x, y in zip(sizes[1:],sizes[:-1])]


# init
# feed forward
# SGD
# update_mini_bash
# Backprop
# Evaluate
# Sigmoid