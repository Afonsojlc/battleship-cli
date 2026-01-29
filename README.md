# battleship-python
A terminal-based Battleship game built with Python. CS101 Portfolio Project.

# 🚢 Battleship in Python

Welcome to my portfolio project! This is a recreation of the classic board game **Battleship**, played entirely in the command line (terminal).

The goal is simple: find and sink all the computer's hidden ships before you run out of attempts!

## 🎮 Features
* **Dynamic Grid:** The board is generated using 2D lists in Python.
* **Randomized Ships:** Ships are positioned randomly at the start of every new game.
* **Input Validation:** The game prevents crashes by handling invalid inputs (e.g., letters instead of numbers) or out-of-bounds coordinates.
* **Visual Feedback:** The board updates after every move ('X' for a hit, '#' for a miss).

## 🛠️ Technologies Used
* **Python 3**: Main game logic.
* **Lists & Loops**: To manage the grid state and game turns.
* **OOP (Object-Oriented Programming)**: The game is structured using Classes (e.g., `Board`) to keep the code organized.
* **Random Module**: For random ship placement.

## 🚀 How to Play
Make sure you have Python 3 installed on your computer.

1. Clone this repository:
   ```bash
   git clone https://github.com/Afonsojlc/battleship-python.git
   ```

2. Enter the project folder:
    ```bash
    cd battleship-python
    ```

3. Run the game:
    ```bash
    python3 code.py
    ```

## 🧠 Challenges & Learnings
This project was developed as part of Codecademy's CS101: Introduction to Programming course.

The biggest challenge was creating the logic to prevent overlapping ships (ensuring two ships don't occupy the same spot) and managing the coordinate system (row/column) in a user-friendly way. Additionally, applying Class and Instance concepts in a real-world scenario helped consolidate my OOP knowledge.

Author: Afonso Carvalho 