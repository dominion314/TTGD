# Self Driving Car
# Games are written along with the visual car as well.
# Importing the libraries
import numpy as np
from random import random, randint
import matplotlib.pyplot as plt
import time

# Importing the Kivy packages. Using Kivy to make the map and add tools to it.
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line
from kivy.config import Config
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock

# Importing the Dqn object from our AI in ai.py. This is where we bring in the brain which is the artifical intelligence Q learning Dqn.
from ai import Dqn

# Adding this line if we don't want the right click to put a red point
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

# Introducing last_x and last_y, used to keep the last point in memory when we draw the sand on the map. Coordinates in memory.
last_x = 0
last_y = 0
n_points = 0
length = 0

# Getting our AI, which we call "brain", and that contains our neural network that represents our Q-function. 
brain = Dqn(5,3,0.9) #Brain is the object, DQN is the class. 5 refers to the state of 5 dimensions to describe the env. 3 is the number of actions -left,stright,right. 0.9 is the gamma parameter for the DQN.
action2rotation = [0,20,-20] #Vector of 3 elements. Actions encoded by 0,1,2. If election is 0 it corresponds to action 0. If 1 it repsonds to 20, so the car goes 20 degrees to the right. If it 2 it will go -20 left.
last_reward = 0 #If doesnt go into sand it will git positive reward if it does then a negative.
scores = [] #Sldiing window for reward so we can make score of the mean score of rewards.

# Initializing the map
first_update = True
def init():
    global sand #An array where the cells will be either 0 or 1 for pixel. All sand starts as zero, once we draw sand they become one.
    global goal_x #train the car to read in upper left corner of the map. (airport)
    global goal_y 
    global first_update
    sand = np.zeros((longueur,largeur))
    goal_x = 20
    goal_y = largeur - 20
    first_update = False

# Initializing the last distance
last_distance = 0 #Current distance from car to the goal

# Creating the car class
#one class for car, one class for the map.
class Car(Widget): 
    
    angle = NumericProperty(0)
    rotation = NumericProperty(0)
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)
    sensor1_x = NumericProperty(0)#Front sensor
    sensor1_y = NumericProperty(0)
    sensor1 = ReferenceListProperty(sensor1_x, sensor1_y)
    sensor2_x = NumericProperty(0)#Left of car
    sensor2_y = NumericProperty(0)
    sensor2 = ReferenceListProperty(sensor2_x, sensor2_y)
    sensor3_x = NumericProperty(0)#Right of car
    sensor3_y = NumericProperty(0)
    sensor3 = ReferenceListProperty(sensor3_x, sensor3_y)
    signal1 = NumericProperty(0)#signals for sent from sensor. Density of each 200x200 square give us the density of sand for each signal.
    signal2 = NumericProperty(0)
    signal3 = NumericProperty(0)

    def move(self, rotation): #Movement of car
        self.pos = Vector(*self.velocity) + self.pos #Position updated into velocity vector
        self.rotation = rotation #How we need to rotate car left or right
        self.angle = self.angle + self.rotation #Update sensor and signals as sensors have rotated by the rotate function
        self.sensor1 = Vector(30, 0).rotate(self.angle) + self.pos #Distance between car and what sensor detects
        self.sensor2 = Vector(30, 0).rotate((self.angle+30)%360) + self.pos
        self.sensor3 = Vector(30, 0).rotate((self.angle-30)%360) + self.pos
        self.signal1 = int(np.sum(sand[int(self.sensor1_x)-10:int(self.sensor1_x)+10, int(self.sensor1_y)-10:int(self.sensor1_y)+10]))/400.#get x coord of sensor and then do -10 + 10, and do it again, and then contain them all from the 20X20 which will come out to 400. This happens for each signal.
        self.signal2 = int(np.sum(sand[int(self.sensor2_x)-10:int(self.sensor2_x)+10, int(self.sensor2_y)-10:int(self.sensor2_y)+10]))/400.
        self.signal3 = int(np.sum(sand[int(self.sensor3_x)-10:int(self.sensor3_x)+10, int(self.sensor3_y)-10:int(self.sensor3_y)+10]))/400.
        if self.sensor1_x>longueur-10 or self.sensor1_x<10 or self.sensor1_y>largeur-10 or self.sensor1_y<10: #get coord when getting too close to wall. If the snesor reaches any if the 4 edges it will set the sense to be 1 which will STOP the car and give a bad reward.
            self.signal1 = 1.
        if self.sensor2_x>longueur-10 or self.sensor2_x<10 or self.sensor2_y>largeur-10 or self.sensor2_y<10:
            self.signal2 = 1.
        if self.sensor3_x>longueur-10 or self.sensor3_x<10 or self.sensor3_y>largeur-10 or self.sensor3_y<10:
            self.signal3 = 1.

class Ball1(Widget):
    pass
class Ball2(Widget):
    pass
class Ball3(Widget):
    pass

# Creating the game class

class Game(Widget):

    car = ObjectProperty(None)
    ball1 = ObjectProperty(None)
    ball2 = ObjectProperty(None)
    ball3 = ObjectProperty(None)

    def serve_car(self):
        self.car.center = self.center
        self.car.velocity = Vector(6, 0)

    def update(self, dt): #This is what will select the action the car has to do. Its the exact output of our neural network. 

        global brain
        global last_reward
        global scores
        global last_distance
        global goal_x
        global goal_y
        global longueur
        global largeur

        longueur = self.width
        largeur = self.height
        if first_update:
            init()

        xx = goal_x - self.car.x
        yy = goal_y - self.car.y
        orientation = Vector(*self.car.velocity).angle((xx,yy))/180.
        last_signal = [self.car.signal1, self.car.signal2, self.car.signal3, orientation, -orientation]
        action = brain.update(last_reward, last_signal) #Returned by brain of car. The object of the DQN that we will be updating takes the last reward and last signal - obtained by the card from the 3 signals + the orientation of the car. Creates output of the DQN network.
        scores.append(brain.score()) 
        rotation = action2rotation[action]
        self.car.move(rotation)
        distance = np.sqrt((self.car.x - goal_x)**2 + (self.car.y - goal_y)**2) #Distance of car to goal.
        self.ball1.pos = self.car.sensor1
        self.ball2.pos = self.car.sensor2
        self.ball3.pos = self.car.sensor3

        if sand[int(self.car.x),int(self.car.y)] > 0: #If car in sand, it will be reduced velocity, will slow to 1.
            self.car.velocity = Vector(1, 0).rotate(self.car.angle)
            last_reward = -1 #Punishment given, worst reward
        else: # otherwise
            self.car.velocity = Vector(6, 0).rotate(self.car.angle) #keep usual speed of 6
            last_reward = -0.2 #getting further away from reward
            if distance < last_distance:
                last_reward = 0.1

        if self.car.x < 10: #If it gets to close to the four edges different rewards are dealt.
            self.car.x = 10
            last_reward = -1
        if self.car.x > self.width - 10:
            self.car.x = self.width - 10
            last_reward = -1
        if self.car.y < 10:
            self.car.y = 10
            last_reward = -1
        if self.car.y > self.height - 10:
            self.car.y = self.height - 10
            last_reward = -1

        if distance < 100: #When car reaches airport in upper left, the goal changes to lower downtown. Update distance from car to goal. 
            goal_x = self.width-goal_x
            goal_y = self.height-goal_y
        last_distance = distance

# Adding the painting tools
# Paint roads and obstacles to the road.
class MyPaintWidget(Widget):

    def on_touch_down(self, touch):
        global length, n_points, last_x, last_y
        with self.canvas:
            Color(0.8,0.7,0)
            d = 10.
            touch.ud['line'] = Line(points = (touch.x, touch.y), width = 10)
            last_x = int(touch.x)
            last_y = int(touch.y)
            n_points = 0
            length = 0
            sand[int(touch.x),int(touch.y)] = 1

    def on_touch_move(self, touch):
        global length, n_points, last_x, last_y
        if touch.button == 'left':
            touch.ud['line'].points += [touch.x, touch.y]
            x = int(touch.x)
            y = int(touch.y)
            length += np.sqrt(max((x - last_x)**2 + (y - last_y)**2, 2))
            n_points += 1.
            density = n_points/(length)
            touch.ud['line'].width = int(20 * density + 1)
            sand[int(touch.x) - 10 : int(touch.x) + 10, int(touch.y) - 10 : int(touch.y) + 10] = 1
            last_x = x
            last_y = y

# Adding the API Buttons (clear, save and load)

class CarApp(App): #To add API buttons - clear, save to the brain, and load brain

    def build(self):
        parent = Game()
        parent.serve_car()
        Clock.schedule_interval(parent.update, 1.0/60.0)
        self.painter = MyPaintWidget()
        clearbtn = Button(text = 'clear')
        savebtn = Button(text = 'save', pos = (parent.width, 0))
        loadbtn = Button(text = 'load', pos = (2 * parent.width, 0))
        clearbtn.bind(on_release = self.clear_canvas)
        savebtn.bind(on_release = self.save)
        loadbtn.bind(on_release = self.load)
        parent.add_widget(self.painter)
        parent.add_widget(clearbtn)
        parent.add_widget(savebtn)
        parent.add_widget(loadbtn)
        return parent

    def clear_canvas(self, obj):
        global sand
        self.painter.canvas.clear()
        sand = np.zeros((longueur,largeur))

    def save(self, obj):
        print("saving brain...")
        brain.save()
        plt.plot(scores)
        plt.show()

    def load(self, obj):
        print("loading last saved brain...")
        brain.load()

# Running the whole thing
if __name__ == '__main__':
    CarApp().run()
