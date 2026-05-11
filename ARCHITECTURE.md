# ARCHITECTURE.md

Written by team-lead before spawning teammates. This is the shared blueprint —
teammates read it to understand what they are building and how their module fits.
Update it when the structure changes; do not let it drift from the actual code.

## Module Structure

- src/game.py: Main Game class, game loop, state management (score, difficulty)
- src/snake.py: Snake class, movement logic, body tracking, growth mechanics
- src/board.py: Grid board state, food placement, collision detection (walls/self)
- src/ui.py: Terminal rendering, user input handling, display update loop
- src/direction.py: Direction enum (UP, DOWN, LEFT, RIGHT) with rotation logic
- src/config.py: Configuration constants (grid size, speeds, colors)

## Interfaces

### board.py
- Board class with:
  - `__init__(width: int, height: int) -> None`
  - `place_food() -> Tuple[int, int]` - returns food position
  - `is_valid_position(x: int, y: int) -> bool` - wall collision check
  - `is_self_collision(x: int, y: int, snake_body: List[Tuple[int, int]]) -> bool`
  - `food_at(x: int, y: int) -> bool` - check if food exists at position
  - `remove_food(x: int, y: int) -> None`

### snake.py
- Snake class with:
  - `__init__(start_x: int, start_y: int) -> None`
  - `get_head() -> Tuple[int, int]` - current head position
  - `get_body() -> List[Tuple[int, int]]` - all body segments
  - `move(direction: Direction) -> None` - advance snake one cell
  - `grow() -> None` - extend body on eating food
  - `check_self_collision() -> bool`

### game.py
- Game class with:
  - `__init__(difficulty: str = "medium") -> None`
  - `start() -> None` - begins game loop
  - `handle_input(key: str) -> None` - process directional input
  - `update() -> bool` - advances game state, returns game_over flag
  - `get_score() -> int`
  - `get_difficulty_speed() -> int` - milliseconds per frame

### ui.py
- UI class with:
  - `render(game_state: GameState) -> None` - draw board, snake, food, score
  - `get_user_input() -> str` - non-blocking input (or blocking with timeout)
  - `show_game_over(score: int) -> None`
  - `show_instructions() -> None`

### direction.py
- Direction enum: UP, DOWN, LEFT, RIGHT
- `rotate_left(dir: Direction) -> Direction`
- `rotate_right(dir: Direction) -> Direction`
- `opposite(dir: Direction) -> Direction`

### config.py
- GRID_WIDTH: int = 20
- GRID_HEIGHT: int = 20
- DIFFICULTY_SPEEDS: Dict[str, int] = {"easy": 200, "medium": 150, "hard": 100}
- FOOD_CHAR: str = "O"
- SNAKE_CHAR: str = "#"
- EMPTY_CHAR: str = " "

## Shared Data Structures

- Position: Tuple[int, int] - (x, y) coordinates
- SnakeBody: List[Tuple[int, int]] - ordered list from head to tail
- GameState: Dict with keys: snake (Snake), food (Position), score (int), game_over (bool)
- Direction: Enum with 4 cardinal directions

## External Dependencies

- Standard library only: `curses` for terminal UI, `enum` for Direction, `random` for food placement
