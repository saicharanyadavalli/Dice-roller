# 🎲 Dice Roll Simulator with ASCII Animation

A fun Python program that simulates the roll of a standard six-sided die with a suspenseful ASCII animation. When the user presses Enter, the script rapidly cycles through numbers 1 to 6, mimicking the spinning of a die. After two quick loops, it reveals the final number randomly selected using `randint`. It's a simple, beginner-friendly project that combines randomness, animations, and terminal output formatting for a cool effect.

## ✅ Approach

- Wait for user input (`Enter`) to begin the roll.
- Use `random.randint(1, 6)` to pick the final outcome.
- Animate the numbers 1 through 6 with a short delay (`0.1s`) between frames.
- Repeat the number cycle twice for suspense.
- Clear the terminal between frames using `os.system('cls' or 'clear')`.
- Display the final rolled number at the end.

## 💡 Solution Description

The program starts by prompting the user to roll the dice. It then uses `random.randint` to select a number between 1 and 6 as the final result. Before revealing it, the script animates a rolling effect by quickly printing numbers 1 to 6 twice, using delays and screen clearing to simulate motion. Finally, it displays the chosen number to the user.

## ▶️ How to Run

1. Save the code in a file called `dice_roll.py`
2. Open a terminal and run:
   ```bash
   python dice_roll.py
