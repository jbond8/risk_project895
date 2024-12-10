# ECON 895 - Project I

## Overview
`utility_functions.py`: Provides utility functions.  
`risk.py`: Contains the stepwise elicitation algorithm.  
`main.py`: Runs the FastAPI web app.  
`lottery.py`: Contains functions to make and print lotteries.  
`holt_laury.py`: Builds and prints Holt-Laury lotteries.  
`helpers.py`: Contains helper functions to solve lottery problems.  
`agent.py`: Contains functions for calculating an agent's expected value, utility, certainty equivalent, etc.  

## Notebooks
All 3 parts of Project 1 are split up into three notebooks to make viewing work easier.

- `ECON895_Project 1_PART 1_Notebook` neatly presents the input and auto stepwise algorithms. They can also be viewed within `risk.py`.
- `ECON895_Project 1_PART 2_Notebook` builds a 2x2 risky coordination game and explores different risk aversion parameters to see if risk aversion affects gameplay.
- `ECON895_Project 1_PART 3_Notebook` outlines how to start the FastAPI web app and walks through the basics of the program.

## FastAPI Web App
A very important part of the project is the web app. Launching it is easy. After cloning the GitHub folder, simply run `fastapi dev main.py` within the terminal. 
You will then be prompted to go to a locally hosted address in your web browser (most likely http://127.0.0.1:8000).

Remember, `ECON895_Project 1_PART 3_Notebook` will provide a brief walkthrough of the web app.

## Preview of FastAPI Web App

<img src="./img/Screenshot 2024-12-09 215225.png" alt="alt text" width="400" />