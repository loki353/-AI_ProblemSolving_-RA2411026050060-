# 🧠 Artificial Intelligence Problem Solving Assignment

## 👨‍💻 Student Details

**Name:** B Lokesh
**Course:** Artificial Intelligence Lab

---

# 📌 Project Overview

This project demonstrates the implementation of fundamental Artificial Intelligence problem-solving techniques through two real-world applications:

1. **Interactive Game AI (Tic-Tac-Toe System)**
2. **Smart Navigation System (Graph Traversal)**

The objective is to design intelligent systems capable of decision-making, optimization, and pathfinding using classical AI algorithms.

---

#  Problem 1: Tic-Tac-Toe AI

##  Description

A web-based interactive Tic-Tac-Toe game where a human player competes against an AI agent. The AI always chooses the optimal move based on search algorithms.

## ⚙️ Algorithms Used

### 🔹 Minimax Algorithm

* Explores all possible game states
* Assumes opponent plays optimally
* Guarantees the best move

###  Alpha-Beta Pruning

* Optimized version of Minimax
* Eliminates unnecessary branches
* Improves performance significantly

##  Working Principle

* The game board is represented as a state space
* AI evaluates each possible move recursively
* Scores are assigned:

  * Win = +1
  * Loss = -1
  * Draw = 0

## 📊 Comparison

| Feature          | Minimax | Alpha-Beta |
| ---------------- | ------- | ---------- |
| Node Exploration | High    | Reduced    |
| Speed            | Slower  | Faster     |
| Accuracy         | Optimal | Optimal    |

## 🖥️ Output

* Interactive gameplay
* AI always makes optimal moves
* Displays winner or draw
* Shows performance comparison

---

# 🎯 Problem 2: Smart Navigation System

## 🧩 Description

A navigation system that finds paths between nodes using graph traversal algorithms. It simulates real-world routing like maps.

## ⚙️ Algorithms Used

### 🔹 Breadth-First Search (BFS)

* Explores level-by-level
* Guarantees shortest path

### 🔹 Depth-First Search (DFS)

* Explores deep paths first
* May not return shortest path

## 🧠 Working Principle

* Graph is represented using adjacency list
* User provides:

  * Start node
  * Goal node
* System traverses graph using BFS and DFS

## 📊 Comparison

| Feature         | BFS           | DFS            |
| --------------- | ------------- | -------------- |
| Path Optimality | Shortest Path | Not Guaranteed |
| Memory Usage    | High          | Low            |
| Traversal Style | Level-wise    | Depth-wise     |

## 🖥️ Output

* Displays path from start to goal
* Shows traversal order
* Compares efficiency of algorithms

---

# 🛠️ Technologies Used

* **Programming Language:** Python
* **Libraries:**

  * math
  * collections
* **Optional GUI:** Streamlit / Tkinter

---

# ⚙️ Installation & Execution

## 🔧 Prerequisites

* Python 3.x installed

## ▶️ Run the Project

```bash
python main.py
```

For GUI (if implemented):

```bash
pip install streamlit
streamlit run app.py
```

---

# 📂 Project Structure

```
AI_ProblemSolving_<RegNo>/
│
├── TicTacToe/
├── Navigation/
├── README.md
```

---

# 📸 Sample Outputs

## Tic-Tac-Toe
## Navigation
**** in the folders ****

# 🚀 Key Features

✔ Intelligent decision-making using AI
✔ Optimal move selection in games
✔ Efficient pathfinding algorithms
✔ Comparison of algorithm performance
✔ Clean and modular code structure

---

---

# 🙌 Acknowledgment

This project was developed as part of the Artificial Intelligence Lab assignment to enhance practical understanding of AI concepts.

---

