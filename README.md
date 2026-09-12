# Number-Ninja

Hey y'all! 

I'm an 18 year old who just started programming and started learning Python. I decided after learning a bit about loops and conditions to create a mini game; a sort of a guess the number game.

## 🎯 About the Project

The game consists of 4 levels:
- Easy => the player must find a number within a range of 1 - 20. Max. number of tries: 5
- Medium => the player must find a number within a range of 1 - 100. Max. number of tries: 8 
- Hard => the player must find a number within a range of 1 - 500. Max. number of tries: 9 
- Impossible => the player must find a number within a range of 1 - 1000. Max. number of tries: 5

The game tells the player if the entered number is lower or higher than the random number and the player is notified if the number is really close to the answer.

Each win earns the player an specific amount of coins that changes depending on the selected level which he can use in the game to purchase items: 
- 🍀 1. The Lucky Charm (Revive on Death)     — 20 Coins")
- 🛡️  2. Smoke Shield (Absorbs 1 Wrong Guess)  — 25 Coins")
- 🧪 3. Heart Container (+2 Extra Lives)      — 30 Coins")
- 🥷  4. Smoke Bomb (First 2 Misses are Free)  — 40 Coins")

I also added a few colors just to make it a bit less "boring and generic".

### Why I Built This:

* To practice working with Python's built-in `random` module.
* To master control flow structures (`while` loops and `if/elif/else` conditional logic).
* To handle basic user input and data type conversion (casting strings to integers).

#### 🧠 What I Learned

* **Input Validation:** I learned how to handle situations where a user accidentally types a letter instead of a number, ensuring the game doesn't crash.
* **State Management:** Tracking the number of attempts the player took to win the game.

##### 📈 Future Improvements

In the future, I plan to expand this project by adding:
* A scoring system or high-score tracker.
* A Graphical User Interface (GUI) using Tkinter.
