import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('https://archive.ics.uci.edu/ml/'
              'machine-learning-databases/iris/iris.data',
               header=None)
df.tail()

class Perceptron(object):
       def __init__(self, eta=0.01, n_iter=50, random_state=1):
           self._eta = eta
           self._n_iter = n_iter
           self._random_state = random_state

       def fit(self, X, y):
           rgen = np.random.RandomState(self._random_state)
           self.w_ = rgen.normal(loc=0.0, scale=0.01,
                                 size= 1 + X.shape[1])
           self.errors_ = []
           for _ in range(self._n_iter):
               errors = 0

               for xi, target in zip(X, y):
                   update = self._eta * (target - self.predict(xi))
                   self.w_[1:] += update * xi
                   self.w_[0] += update
                   errors += int(update != 0.0)
               self.errors_.append(errors)
           return self

       def net_input(self, X):
           """Calculate net input"""
           return np.dot(X, self.w_[1:]) + self.w_[0]

       def predict(self, X):
           """Return class label after unit step"""
           return np.where(self.net_input(X) >= 0.0, 1, -1)



X = np.array([[1] * 10] * 10)
rgen = np.random.RandomState(1)
w_ = rgen.normal(loc=0.0, scale=1,
                          size= 1 + X.shape[1])
print(rgen)
print(w_)



