Reinforcement Learning 

What is it? An agent will perform an action in an evnironment and the state will change each time leading to a reward or no reward. By doing so
the agent learns the environment and better navigates. The performance of the agent is rewarded dependent on its actions. If the agent compeletes
the correct actions at the correct time with the correct order, leads to completion of a task. You reinforce the actions of the agent,
based on positive or negative returns. In terms of AI, think of reinforcement learning with dogs except with AI the rewards are +1 or -1.

Reinforcement algorythms controll all the degrees of freedom along with the rewards for the actions of your AI. Through this learning process
AI can outperform pre-programmed machines. It can learn as it discovers what its goals and rewards are. 



Bellman Equation

Richard Ernest Bellman was a mathematician who developed his equation in 1953. 

The Bellman Equation states that the expected long-term reward for a given action is equal to the immediate reward from the current action combined with the expected reward from the best future action taken at the following state. Many actions can be taken and for every possible action the Bellman equation will determine values based on maximum reward. Its here to solve the problem of opportunity cost or the time value of money.

Bellman Equation = V(s) = maxa(R(s,a) + yV(s'))

Explanation = The expected returned Value(V) at the current state(s) is equal to the maximum value of any possible action(a) for the expected reward(R) for taking that action(a) at state(s)...plus the discount factor(gamma -yV) multipled by the value of the next state(s').


Equation for Q Values = Q(s,a) = r + γ(max(Q(s’,a’))

Explanation = The "Q" values for a given state(s) and action(a) should represent the current reward(r) plus the maximum discounted future reward(y)
            expected according to our own table for the next state(s) we would end in.



Simply - This defines the curent rewards from future rewards depending on our current state and the potential rewards of the future state. 
Why is it important - Data can be updated by using these accurate measures into tables of future rewards allowing for agents to make better decisions.

Check out the bellman_equation.py file to see how this is done in FrozenLake. WHen you run the code it basically gives you a 4 x 16 matrix that contains the values of each individual cell based on the perceived values in the script. These values could be transposed onto a visual grid to help the agent navigate an environment and its obstacles. 

Using Tensorflow you can apply this Q Table to a neural network. However, what you make up for in flexibility you lose in stability. 





The Plan


Markov Decision Process


Policy vs Plan


Living Penalty


Q-Learning Inuition


Temporal Difference