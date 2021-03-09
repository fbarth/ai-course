# Code for Artificial Intelligence course

I am using this project as a support to the exercises in an Artificial Intelligence course that is part of an undergraduate course at [ESPM](http://international.espm.br/), Computer Information Systems. The topics discussed in the course are: 

1.	Artificial Intelligence Introduction;
2.	Intelligent Agents;
3.	Solving Problems by Searching;
4.	Informed Search Methods;
5.	Game Playing;
6.	Reinforcement Learning (Here, I present the concept of Learning from Observations, Supervised Learning and Unsupervised Learning. However, I have a specific course to discuss those topics. You can access this material [here](https://github.com/fbarth/ml-espm)).

If you prefer, you can check the description of this course in this [video](https://www.youtube.com/watch?v=LsD24XDhIHg). 

## How this project is structured 

We have four (4) folders:

* *docs*: this folder has several documents describing concepts, algorithms and projects. All content is in Portuguese. 

* *search*: this folder has implementations related to solving problem by searching, and informed search methods. I suggest to start from this folder in order to understand all the implementations (search, games, and reinLearn).

* *games*: this folder keeps source code related to game playing.

* *reinLearn*: this folder has source code related to reinforcement learning. Some examples are using the project [Gym](https://gym.openai.com/).

## How to setup the environment

In order to avoid any configuration problem, I recommend to create a virtual environment: 

````bash
virtualenv venv
source venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
````

To quit the virtual environment, type `deactivate`. If you already have the virtual environment configured then type `source venv/bin/activate`. 


