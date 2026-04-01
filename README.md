# 🎮 Ultimate Number Guessing Game (Python)

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge">
  <img src="https://img.shields.io/badge/Level-Intermediate-orange?style=for-the-badge">
</p>

---

## 📌 Overview

This is an advanced version of the classic Number Guessing Game built using Python.
The project goes beyond basic gameplay by adding scoring, timing, difficulty levels, and a persistent leaderboard system.

It’s designed as a mini real-world project to demonstrate core programming concepts in a practical way.

---

## 🚀 Features

### 🎯 Difficulty Levels

* Easy → Range: 1–50 (10 attempts)
* Medium → Range: 1–100 (7 attempts)
* Hard → Range: 1–200 (5 attempts)

### ⏳ Limited Attempts

Each level restricts the number of guesses, increasing challenge and strategy.

### ⭐ Score System

* Starts from 100
* Each wrong guess reduces score by 10
* Fewer attempts = higher score

### ⏱️ Timer System

* Tracks how fast the player solves the game
* Displays total time after completion

### 🏆 Leaderboard System

* Stores:

  * Player Name
  * Score
  * Time Taken
  * Status (WIN / LOSE)
* Saves data in `leaderboard.txt`
* Automatically sorts and displays top scores

### 🔁 Replay System

* Play multiple rounds without restarting the program

### 📢 Smart Hint System

* 📉 Too low
* 📈 Too high
* 🎉 Correct

---

## 🖥️ Demo (CLI Preview)

```
🎮 Ultimate Number Guessing Game

1. Play Game
2. View Leaderboard
3. Exit
```

---

## 🛠️ Technologies Used

* Python 3
* Built-in modules:

  * random
  * time
* File Handling (.txt)

---

## ▶️ How to Run

```bash
python main.py
```

---

## 🧠 How It Works

1. User selects a difficulty level
2. System generates a random number
3. Player guesses within limited attempts
4. Score updates dynamically
5. Time is recorded
6. Result is saved to file
7. Leaderboard shows top players

---

## 📊 Example Leaderboard

```
1. Rahman | Score: 90 | WIN  | Time: 8.52s
2. Alex   | Score: 70 | LOSE | Time: 15.21s
```

---

## ⚠️ Notes

* `leaderboard.txt` is auto-created after first game
* Delete old file if format issues occur

---

## 📚 Learning Outcomes

* Game logic design
* Loop & condition handling
* File read/write operations
* Data sorting
* Time tracking
* Building structured Python applications

---

## ✨ Future Improvements

* GUI version (Tkinter)
* Web version (HTML + JS)
* Database integration (SQLite)
* Multiplayer mode
* Sound effects

---

## 🙌 Contribution

Feel free to fork, improve, and submit pull requests.

---

## 📌 Author

**Abdur Rahman**

```Computer & Communication Engineering Student```

Aspiring Software Developer 🚀

---

⭐ If you like this project, give it a star!
