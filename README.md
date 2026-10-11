# 🚢 Battleship CLI

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Tests](https://img.shields.io/badge/tests-7%20passed-brightgreen)
![License](https://img.shields.io/badge/license-MIT-green)

> A terminal-based recreation of the classic naval game **Battleship**, built with Python using Object-Oriented Programming (OOP). The player guesses grid coordinates to find and sink all hidden ships before running out of attempts.

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

## ✨ Features

* **Object-Oriented Design:** A `Board` class encapsulates the grid state, coordinate tracking, and game rules.
* **Input Validation:** Handles non-numeric inputs, out-of-bounds coordinates, and repeated guesses without penalizing player attempts.
* **Configurable Settings:** Adjustable grid dimensions and ship count (defaults to a 5x5 board with 3 ships).
* **Game Over Reveal:** Displays remaining hidden ship locations if the player runs out of attempts.
* **Automated Unit Tests:** Full test suite using Python's built-in `unittest` module.

---

## 🛠️ Tech Stack

* **Language:** Python 3.10+ (Standard Library only — no external dependencies)
* **Testing:** `unittest`
* **Concepts:** Object-Oriented Programming, state management, input validation

---

## 📁 Project Structure

```text
battleship-cli/
├── tests/
│   ├── __init__.py
│   └── test_board.py      # Unit test suite
├── .gitignore
├── battleship.py          # Core Board class and CLI game loop
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites
* **Python 3.10+** installed on your system.

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

## 🧪 Running Tests

To run the automated test suite:

```bash
python -m unittest discover -s tests -v
```

Expected output:
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

## 👤 Author

**Afonso Carvalho**  
* GitHub: [@Afonsojlc](https://github.com/Afonsojlc)  
* LinkedIn: [Afonso Carvalho](https://www.linkedin.com/in/afonso-carvalho-64796328a/)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
