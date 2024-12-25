# Pong Game in Python: A Retro Arcade Experience

This repository contains a Python implementation of a two-player Pong game. The game is designed with object-oriented programming (OOP) principles and is split into four modular components for better organization and functionality.

## Features
- **Two-player Gameplay**: Players control paddles on opposite sides of the screen.
- **Custom Controls**: 
  - Left paddle: 'W' (up) and 'S' (down)
  - Right paddle: 'PgUp' (up) and 'PgDn' (down)
- **Scoreboard**: Tracks the score, with the game ending when one side reaches 10 points.
- **Dynamic Ball Movement**: The ball starts at the center and moves across the screen, bouncing off paddles and walls.

## Project Structure
The project is divided into the following components:

1. **main.py**:
   - Combines all modules to ensure the game functions seamlessly.
   - Manages the game loop and overall game logic.

2. **paddle.py**:
   - Creates and manages the two paddles on opposite sides of the screen.
   - Assigns controls for moving the paddles up and down.

3. **ball.py**:
   - Handles the creation and movement of the ball.
   - Manages ball collisions with paddles and walls.

4. **scoreboard.py**:
   - Displays and updates the score for each player.
   - Ends the game when a player reaches 10 points.

## How to Play
1. Clone this repository:
   ```bash
   git clone https://github.com/AkhilCh54/Pong-Game-in-Python-A-Retro-Arcade-Experience.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Pong-Game-in-Python-A-Retro-Arcade-Experience
   ```
3. Run the game:
   ```bash
   python main.py
   ```
4. Controls:
   - Left paddle: Use 'W' to move up and 'S' to move down.
   - Right paddle: Use 'PgUp' to move up and 'PgDn' to move down.

5. Score 10 points to win the game!

## Future Enhancements
- Add sound effects for paddle hits and scoring.
- Introduce power-ups or special ball movements.
- Add AI-controlled paddle for single-player mode.

---
Enjoy the game!

