# AI for Self Driving Car
# Brain of the Car
# Importing the libraries

import numpy as numpy
import random
import os #Load and save the brain
import torch #Pytorch for nueral network, better than tensor.
import torch.nn as nn #deep neural network and reutnr output for q values of diff action when reciving the three sensors data. most essential
import torch.nn.functional as f#shortcut to functional package that contains function for NN as f. We will be using ooberloss?
import torch.optim as optim#optimizier for stochasstics
import torch.autograd as autograd
from torch.autograd import Variable

#Creating the architecture of the Neural Network. A class is the model of something you want to build. Well create two functions that defines the variables of the NN.
#A function of for the 5 inputs, a function for th hidden layer, a function for the output layer. We will then create a forward function that will activate the signals in the NN.
#A rectifier function for nonlinear function. 1 Q value for each action.

class Network(nn.Module): #In this class we will use inheritance to inerit all tools of parent class. NN.module is the parent class. Build architecture. 

    def __init__(self, input_size, nb_action):
        super(Network, self).__init__()#super function inherits from nn.Module. This make sit able to use the tools of module. Specify the network
        self.input_size = input_size #New variable to attach to object. Youre specifying 5 input neurons in the input layer each time youre creating an object from the input class
        self.nb_action = nb_action #Number of output neurons.
        self.fc1 = nn.Linear(input_size, 30) #FC1 is a variable of the object self. All the neurons of the input layer will have all the inputs of hidden layer. In feature is input size, out feature is num of neurons in second layer. You can add more than 30 layers, this is where you can experiment with the connection rate.
        self.fc2 = nn.Linear(30, nb_action) #Hidden layer and outer layer. Can also change the 30 here. 
    
    def forward(self, state): #Activate neurons in the network and to return Q values as the output of our network. Activates neurons 
        x = F.relu(self.fc1(state)) #relu is the rectifier function for F. Neuron state for first full conneciton.
        q_values = self.fc2(x) #Return output neurons or Q values. We use Q learning to get data for our actions.
        return q_values #returns Q values for each connection possible.

# Implementing Experience Replay

class ReplayMemory(object): 
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.memory = []
    
    def push(self, event):
        self.memory.append(event)
        if len(self.memory) > self.capacity:
            del self.memory[0]
    
    def sample(self, batch_size):
        samples = zip(*random.sample(self.memory, batch_size))
        return map(lambda x: Variable(torch.cat(x, 0)), samples)

# Implementing Deep Q Learning

class Dqn():
    
    def __init__(self, input_size, nb_action, gamma):
        self.gamma = gamma
        self.reward_window = []
        self.model = Network(input_size, nb_action)
        self.memory = ReplayMemory(100000)
        self.optimizer = optim.Adam(self.model.parameters(), lr = 0.001)
        self.last_state = torch.Tensor(input_size).unsqueeze(0)
        self.last_action = 0
        self.last_reward = 0
    
    def select_action(self, state):
        probs = F.softmax(self.model(Variable(state, volatile = True))*100) # T=100
        action = probs.multinomial(num_samples=1)
        return action.data[0,0]
    
    def learn(self, batch_state, batch_next_state, batch_reward, batch_action):
        outputs = self.model(batch_state).gather(1, batch_action.unsqueeze(1)).squeeze(1)
        next_outputs = self.model(batch_next_state).detach().max(1)[0]
        target = self.gamma*next_outputs + batch_reward
        td_loss = F.smooth_l1_loss(outputs, target)
        self.optimizer.zero_grad()
        td_loss.backward(retain_graph = True)
        self.optimizer.step()
    
    def update(self, reward, new_signal):
        new_state = torch.Tensor(new_signal).float().unsqueeze(0)
        self.memory.push((self.last_state, new_state, torch.LongTensor([int(self.last_action)]), torch.Tensor([self.last_reward])))
        action = self.select_action(new_state)
        if len(self.memory.memory) > 100:
            batch_state, batch_next_state, batch_action, batch_reward = self.memory.sample(100)
            self.learn(batch_state, batch_next_state, batch_reward, batch_action)
        self.last_action = action
        self.last_state = new_state
        self.last_reward = reward
        self.reward_window.append(reward)
        if len(self.reward_window) > 1000:
            del self.reward_window[0]
        return action
    
    def score(self):
        return sum(self.reward_window)/(len(self.reward_window)+1.)
    
    def save(self):
        torch.save({'state_dict': self.model.state_dict(),
                    'optimizer' : self.optimizer.state_dict(),
                   }, 'last_brain.pth')
    
    def load(self):
        if os.path.isfile('last_brain.pth'):
            print("=> loading checkpoint... ")
            checkpoint = torch.load('last_brain.pth')
            self.model.load_state_dict(checkpoint['state_dict'])
            self.optimizer.load_state_dict(checkpoint['optimizer'])
            print("done !")
        else:
            print("no checkpoint found...")
