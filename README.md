# Python-Project
My first Project in Python, where I created a simple Snake, Water, Gun game. 

# Snake, Water, Gun Game

Welcome to the **Snake, Water, Gun** game, a simple Python implementation of the popular hand game similar to "Rock, Paper, Scissors." In this game, the player competes against the computer by choosing between Snake, Water, and Gun.

## How the Game Works

- **Snake (s)**: Defeats Water, but loses to Gun.
- **Water (w)**: Defeats Gun, but loses to Snake.
- **Gun (g)**: Defeats Snake, but loses to Water.

The game randomly chooses a move for the computer and compares it with the player's choice to determine the winner.

## How to Play

1. **Run the Script**: Start the game by running the Python script.
2. **Make a Choice**: You'll be prompted to choose between Snake, Water, or Gun using the abbreviations:
   - `s` for Snake
   - `w` for Water
   - `g` for Gun
3. **View the Result**: The computer will make its choice, and the result will be displayed, indicating whether you won, lost, or if it was a tie.

## Example

```python
# Sample Output
YOU'VE ENTERED THE GAME "SNAKE, WATER, GUN"!

Use the Following abbreviations: 
s: Snake
w: Water 
g: Gun

Choose Snake, Water or Gun as per the abbreviations used: s
You chose 'Snake' 
Computer chose 'Water'

RESULT---> CONGOO, You WON the match!
