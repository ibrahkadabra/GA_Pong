# GA_Pong
This project implements the classic game of Pong with an exciting twist you can train AI agent and play against it.
The ball and paddles speed increase each time a ball hit the paddle to make it harder 
When the ball hit a paddle a small randomness will be added so that the AI agents won't be able to find a position where can they hit the ball without moving 
The neural network will take as input the y of ball, the y of the paddle and the distance between the ball and the paddle.
You can make small changes in the code to make two agents play agianst each other at the end instead of trying the game by yourself.

# About NEAT
NEAT (NeuroEvolution of Augmenting Topologies) is a powerful algorithm in the field of artificial intelligence and evolutionary computation. It allows neural networks to evolve, grow in complexity, and learn to perform tasks through a process akin to biological evolution.

# Gameplay
In this version of Pong, you can play aginst the best AI agent from all of the generation, powered by NEAT, compete against each other in an intense game of Pong. The agents autonomously learn to control the paddles and compete to score points. It's an intriguing showcase of how AI can learn and adapt to gaming environments.

# Features
NEAT algorithm: Utilizes NEAT to evolve neural networks that control the paddles in Pong.
The ball and paddles speed increase each time a ball hit the paddle to make it harder 
Customizable parameters: Adjust various parameters such as population size, mutation rates, and neural network structure to observe different behaviors in the AI agents.
The "fitness_criterion     = mean" so that we will guarantee that the last agent choosed will be the best among other good agents but this will slow down the training a lot so it is better to change it to max if you don't have time.

# How to Run
Clone the repository to your local machine.
Install the required dependencies.
Run the main script to start training the AI agents.
Challenge the AI and let's see if you will have a chance against him or not.

# Requirements
Python 3.x
NEAT Python library
Pygame
