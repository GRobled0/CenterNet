import numpy as np
import math


class kalman_filter():
  def __init__(self):

    self.X = 0 #estado previo
    self.P = 0.05 #std²
    self.R = 2 #covarianza del ruido medida
    self.Q = 2 #covarianza del ruido proceso
    self.H = 1
    self.index = 0
    self.old_frame = [[0.0, 0.0, 0.0, 0.0, 0.0]] #centro(x, y) distancia X P
    self.new_frame = [[0.0, 0.0, 0.0, 0.0, 0.0]]


  def predict(self, dets):
    self.index = 0
    for item in self.new_frame:
      distxy = math.sqrt((item[0] - (dets[0] + dets[2])/2.0)**2 + (item[1] - (dets[1] + dets[3])/2.0)**2)
      distz = math.sqrt((item[2] - dets[5])**2)
      if distxy < 10 and distz < 0.1: #misma zona
        break
      self.index = self.index + 1

    self.new_frame[self.index][4] = self.new_frame[self.index][4] + self.Q

    #if self.X == 0:
    #  self.X = dets[5]
    #else:
      #self.X = self.A*self.X #+ self.B*self.dt
   #   self.P = self.P + self.Q
    self.update(dets[5])
    return self.new_frame[self.index][3]


  def update(self, z):
     e = self.H * self.new_frame[self.index][3]
     E = self.H*self.new_frame[self.index][4]*self.H
     y = z - e
     Z = self.R + E
     K = self.new_frame[self.index][4]*self.H/Z
     self.new_frame[self.index][3] = self.new_frame[self.index][3] + K * y
     self.new_frame[self.index][4] = self.new_frame[self.index][4] - K *self.H*self.new_frame[self.index][4]

  def frame_update(self, frame):
    self.old_frame = self.new_frame.copy()
    self.new_frame = []
    for item in frame:
      data = []
      data.append((item[0] + item[2])/2.0)
      data.append((item[1] + item[3])/2.0)
      data.append(item[5])
      flag = 0
      for old_item in self.old_frame:
        distxy = math.sqrt((old_item[0] - data[0])**2 + (old_item[1] - data[1])**2)
        distz = math.sqrt((old_item[2] - data[2])**2)
        if distxy < 50 and distz < 0.5: #misma zona
          flag = 1
          data.append(old_item[3])
          data.append(old_item[4])
          break
      if flag == 0:
        data.append(item[5])
        data.append(0.05)
      self.new_frame.append(data)
          
        



