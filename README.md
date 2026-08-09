# Alien Invasion: Side Strike - Track 1
## Video Link: (Coming Soon)
### Project Overview

Alien Invasion: Side Strike is a side scrolling arcade shooter created by modifying and expanding the Alien Invasion starter project.

The vertical shooter mechanics were redesigned so the player controls
a ship positioned on the left side of the screen. The ship moves vertically
and fires horizontal laser projectiles at alien formations approaching from the right.

As the player advances through levels, the alien fleet changes formation and increases in speed and movement difficulty.

Track 1 - Custom Game Mechanics

### Features

- Side-scrolling gameplay
- Player ship positioned on the left side of the screen
- Vertical ship movement
- Horizontal laser firing
- One alien destroyed per laser
- Multiple alien fleet formations
- Vertical alien fleet movement
- Increasing difficulty by level
- Score tracking
- Persistent high score
- Remaining-life display
- Level display
- Laser and impact sound effects
- Play button and game-over state
- High score saved using JSON

### Alien Formations

The alien fleet changes formation as the player progresses through the game.

- Level 1: Rectangle
- Level 2: Wedge
- Level 3: Diamond
- Level 4: Zigzag
- Level 5: Split Columns

The formation cycle repeats on later levels while enemy speed and difficulty continue to increase.

### Controls

- Up Arrow: Move ship upward
- Down Arrow: Move ship downward
- Spacebar: Fire laser
- Q: Quit the game
- Mouse: Click the Play button

### Installation

Python and Pygame are required.

Install the project dependencies with:

```bash
python -m pip install -r requirements.txt