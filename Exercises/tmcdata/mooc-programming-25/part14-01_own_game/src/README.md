# HumbleBot Wants To Retire Alive
 
A pygame game for the University of Helsinki Python Programming MOOC — Part 14 final project.
 
## How to Play
 
You are HumbleBot, a robot with one dream: **retire alive**. Collect coins to build your wallet, avoid the monsters, and reach the retirement door before they eat you.
 
### Controls
 
| Key | Action |
|-----|--------|
| ← → ↑ ↓ | Move HumbleBot |
| R | Restart after game over |
| Q | Quit the game |
 
### Goal
 
Collect **a certain amount of coins, your joy to find out how many,** to become retirement eligible, then walk into the **door** in the centre of the screen. The door will stay locked until you have enough in your wallet.
 
### Watch out
 
- Monsters chase you and get faster as more spawn
- The more coins you collect, the greedier you are, **the more difficult it'll get to reach the door** due to two mysterious side-effects, so choose your route wisely
- If a monster catches you before you retire, it's game over

## Features
 
- Player-controlled sprite with arrow keys and screen boundaries
- 100 collectible coins that wriggle around the screen
- 5 monsters that hunt the player
- Wallet counter and debug HUD showing player speed and max monster speed
- Robot grows in slows as wallet increases
- Retirement win condition — reach the door with wallet ≥ ?? coins
- Game over and retirement screens with restart option

## Requirements
 
```
pygame
```
 
Install with:
 
```bash
pip install pygame
```
 
## Running the Game
 
```bash
cd src
python main.py
```
 
The following image files must be present in the `src/` folder (included in the repo):
 
- `robot.png`
- `monster.png`
- `coin.png`
- `door.png`
## Project Structure
 
```
src/
├── main.py          # All game logic
├── robot.png
├── monster.png
├── coin.png
└── door.png
```
 
## Known Limitations
 
- The `lives` variable is tracked but not yet used — HumbleBot currently has one shot
- Coins can wander off screen edges
 