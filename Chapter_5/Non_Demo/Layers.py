import numpy as np
import function
func = function.function()

class Add_Layer:
	def __init__(self):
		pass

	def forward(self,x,y):
		out = x + y
		return out

	def backward(self,dout):
		dx = dout * 1
		dy = dout * 1
		return dx, dy

class Multi_Layer:
	def __init__(self):
		self.x = None
		self.y = None

	def forward(self,x,y):
		self.x = x
		self.y = y
		out = x * y

		return out

	def backward(self,dout):
		dx = dout * self.y
		dy = dout * self.x

		return dx, dy

class ReLU_Layer:
	def __init__(self):
		self.mask = None

	def forward(self,x):
		self.mask = (x <= 0)
		out = x.copy()
		out[self.mask] = 0

		return out

	def backward(self,dout):
		dout[self.mask] = 0
		dx = dout

		return dx

class Sigmoid_Layer:
	def __init__(self):
		self.out = None

	def forward(self,x):
		out = 1 / (1 + np.exp(-x))
		self.out = out

		return out

	def baclward(self, dout):
		dx = dout * (1 - self.out) * self.out

		return dx

class Affine_Layer:
	def __init__(self,W,b):
		self.W  = W
		self.b  = b
		self.x  = None
		self.dW = None
		self.db = None

	def forward(self,x):
		self.x = x
		out = np.dot(self.x,self.W) + self.b

		return out

	def backward(self, dout):
		dx = np.dot(dout, self.W.T)
		self.dW = np.dot(self.x.T, dout)
		self.db = np.sum(dout, axis = 0)

		return dx

class Softmax_with_loss_Layer:
	def __init__(self):
		self.loss = None
		self.y    = None
		self.t    = None

	def forward(self,x,t):
		self.t = t
		self.y = func.softmax(x)

	def backward(self,dout = 1):
		batch_size = self.t.shape[0]
		dx = (self.y - self.t) / batch_size

		return dx