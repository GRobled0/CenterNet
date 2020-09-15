import torch
from torch import optim
import matplotlib.pyplot as plt
import csv
import torch.nn as nn
import numpy as np
import pandas as pd
from torch.autograd import Variable
import torch.nn.functional as F


#hiperparametros
EPOCH = 1000
LR = 0.0001
n_batches = 252



class Network(nn.Module):
    def __init__(self, ):
        super(Network, self).__init__()
        # parametros
        self.inputSize = 2
        self.outputSize = 1
        self.hiddenSize = 2

        #definicion del modelo
        self.hidden1 = nn.Linear(self.inputSize, self.hiddenSize)
        self.hidden2 = nn.Linear(self.hiddenSize, self.hiddenSize)
        self.output = nn.Linear(self.hiddenSize, self.outputSize)

        
    def forward(self, x):
        z = F.leaky_relu(self.hidden1(x))
        z = F.leaky_relu(self.hidden2(z))
        o = F.leaky_relu(self.output(z))
        return o
    
        
    def saveWeights(self, model):
        # we will use the PyTorch internal storage functions
        torch.save(model, "prueba")
        # you can reload model with all the weights and so forth with:
        # torch.load("NN")

file_input = "inputs.csv"
file_targets = "outputs.csv"
data_raw = pd.read_csv(file_input, delimiter = ',')
data = data_raw.iloc[[1]]
inputs = torch.Tensor(data.values).unsqueeze(1)


target_raw = pd.read_csv(file_targets, delimiter = ',')
target = target_raw.iloc[[1]]
targets = torch.Tensor(target.values)

model = Network()

loss_function = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), LR)

losses = []

for e in range(1, EPOCH+1):

  for b in range(2, n_batches):

    hidden = None
    pred = model.forward(inputs)
    loss = loss_function(targets, pred)
    optimizer.zero_grad()

    loss.backward()
    optimizer.step()
    losses.append(loss.item())

    data = data_raw.iloc[[b]]
    target = target_raw.iloc[[b]]
    inputs = torch.Tensor(data.values).unsqueeze(1)
    targets = torch.Tensor(target.values)

  if e%1 == 0:
    print("epoch: ", e, " ...Loss function: ", losses[-1])

model.saveWeights(model)

file_input = "input_test.csv"
file_targets = "outputs_test.csv"
input_test = pd.read_csv(file_input, delimiter = ',')
inputs = torch.Tensor(input_test.values).unsqueeze(1)
target_test = pd.read_csv(file_targets, delimiter = ',')
targets = torch.Tensor(target_test.values)

pred = model.forward(inputs)

p = pred.detach().numpy()
t = targets.detach().numpy()

absolute_error = 0

for i in range(0,target_test.size):
  error = (p[i] - t[i])/t[i]
  if error < 0:
    error = - error
  absolute_error = absolute_error + error

absolute_error = (absolute_error*100)/target_test.size
print('error:')
print(absolute_error,'%')
