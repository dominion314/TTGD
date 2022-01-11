import numpy as numpy
import random
import os #Load and save the brain
import torch #Pytorch for nueral network, better than tensor.
import torch.nn #deep neural network and reutnr output for q values of diff action when reciving the three sensors data. most essential
import torch.nn.functional as f#shortcut to functional package that contains function for NN as f. We will be using ooberloss?
import torch.optim as optim#optimizier for stochasstics
import torch.autograd as autograd
from torch.autograd import Variable

#Creating the architecture of the Neural Network. A class is the model of something you want to build. Well create two functions that defines the variables of the NN.
#A function of for the 5 inputs, a function for th hidden layer, a function for the output layer. We will then create a forward function that will activate the signals in the NN.
#A rectifier function for nonlinear function. 1 Q value for each action.

class Network(nn.Module): #In this class we will use inheritance to inerit all tools of parent class. NN.module is the parent class.

    def __init__(self, input_size, nb_action)
    super(Network, self).__init__()#super function inherits from parent. This make sit able to use the tools of module. Specify the network
