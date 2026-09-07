# 🚢 Battleship CLI

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Tests](https://img.shields.io/badge/tests-7%20passed-brightgreen)
![License](https://img.shields.io/badge/license-MIT-green)
![Architecture](https://img.shields.io/badge/OOP-Clean%20Architecture-orange)

A clean, terminal-based recreation of the classic naval strategy game **Battleship**, built with Python and Object-Oriented Programming (OOP).

The player takes command of a naval radar system to locate and sink all hidden enemy ships across uncharted waters before running out of attempts.

---

## 🎮 Gameplay Preview

```text
=============================================
        🚢 BATTLESHIP CLI GAME 🚢        
=============================================
Locate and sink all hidden enemy ships!
Legend: [O] Unexplored Sea | [X] Ship Sunk | [#] Missed Shot | [S] Revealed Ship

  0 1 2 3 4
0 O O # O O
1 O X O O O
2 O O O # O
3 O O O O O
4 O # O O X

Attempts remaining: 6
Enemy ships remaining: 1
Select ROW (0-4): 
```

---

## ✨ Key Features

* **Clean OOP Architecture:** Fully encapsulated `Board` class managing the grid state, coordinate tracking, and game rules.
* **Smart Input Validation:** Catches non-numeric entries (`try/except ValueError`) and validates boundaries (`0 <= coord < size`).
* **Non-Punitive Retries:** Invalid inputs, out-of-bounds coordinates, or repeated shots alert the player without wasting attempts.
* **Dynamic Grid Scaling:** Flexible board size and ship count parameters (defaults to 5x5 grid with 3 hidden ships).
* **End-Game Ship Reveal:** On game over, the board displays the exact positions where the remaining enemy fleet was hiding (`S`).
* **Automated Unit Testing:** Includes a full suite of unit tests with Python's built-in `unittest` framework.

---

## 🛠️ Tech Stack & Concepts

* **Language:** Python 3.10+ (Standard Library only - zero external dependencies)
* **Design Patterns:** Object-Oriented Programming (Encapsulation, State Management)
* **Testing:** `unittest` framework covering bounds, duplicate shots, hits/misses, and win conditions
* **Code Style:** PEP 8 compliance with type hinting (`typing.List`, `typing.Set`, `typing.Tuple`)

---

## 📁 Project Structure

```text
battleship-cli/
├── tests/
│   ├── __init__.py
│   └── test_board.py      # Automated unit test suite
├── .gitignore             # Python environment and cache ignores
├── battleship.py          # Core Board class and CLI game loop
└── README.md              # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites
Make sure you have **Python 3.10+** installed on your system.

### 1. Clone the repository
```bash
git clone https://github.com/Afonsojlc/battleship-cli.git
cd battleship-cli
```

### 2. Run the game
```bash
python battleship.py
```

---

## 🧪 Running Unit Tests

The test suite validates board dimensions, ship collision prevention, coordinate bounds, duplicate guesses, and state transitions:

```bash
python -m unittest discover -s tests -v
```

Output:
```text
test_board_initialization ... ok
test_miss_shot ... ok
test_out_of_bounds_guess ... ok
test_repeated_guess ... ok
test_reveal_ships_display ... ok
test_ships_within_bounds ... ok
test_successful_hit ... ok

Ran 7 tests in 0.001s
OK
```

---

## 🧠 Challenges & Learnings

* **Collision-Free Placement:** Used Python `set` data structures to ensure generated ship coordinates never overlap ($O(1)$ lookup time).
* **Decoupled Game Logic:** Separated board state transitions from presentation messages, allowing robust testability and clean CLI rendering.
* **Defensive Error Handling:** Ensured resilient gameplay that gracefully guides the user through invalid inputs without crashing.

---

## 👤 Author

**Afonso Carvalho**  
* GitHub: [@Afonsojlc](https://github.com/Afonsojlc)
* LinkedIn: [Afonso Carvalho](https://www.linkedin.com/in/afonso-carvalho-64796328a/)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
