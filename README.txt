Project: GUI Calculator
Author: Omid Shah Amir Sayed

Description
------------
This project is a graphical calculator written in Python using the Tkinter library.

The program provides a simple interface that allows the user to perform basic
mathematical operations such as addition, subtraction, multiplication and division.
Additional functions like square root, percentage, and power are also implemented.

How the Program Works
---------------------
The program is built using an event-driven structure.

1. The graphical interface (GUI) is created using Tkinter.
   It contains:
   - a display field where numbers appear
   - buttons for numbers and operations

2. Each button is connected to the function:
   
   button_clicked()

   This function receives the button value and decides what action to perform.

3. Mathematical calculations are handled using Python functions:
   - eval() evaluates expressions like "5+3*2"
   - math.sqrt() calculates square roots

4. The calculator also supports keyboard input through the key_pressed() function.

Project Status
--------------
This calculator is functional but still a work in progress.
Future improvements could include:
- improved visual design
- better button layout
- additional mathematical functions.

Running the Program
-------------------
You can run the calculator by double-clicking:

Calculator.exe

Python is not required for running the executable.