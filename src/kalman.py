import numpy as np


class kalman_filter():
  def __init__(self):

    self.X = 0 #estado previo
    self.P = 0.05 #std²
    self.R = 2 #covarianza del ruido medida
    self.Q = 2 #covarianza del ruido proceso
    self.H = 1


  def predict(self, dets):
    if self.X == 0:
      self.X = dets[5]
    else:
      #self.X = self.A*self.X #+ self.B*self.dt
      self.P = self.P + self.Q
      self.update(dets[5])
    return self.X


  def update(self, z):
     e = self.H * self.X
     E = self.H*self.P*self.H
     y = z - e
     Z = self.R + E
     K = self.P*self.H/Z
     self.X = self.X + K * y
     self.P = self.P - K *self.H*self.P



