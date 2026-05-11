import time
from typing import Dict

from config import GRID_WIDTH, GRID_HEIGHT, DIFFICULTY_SPEEDS
from direction import Direction, opposite
from board import Board
from snake import Snake
from ui import UI


class GameState:
    def __init__(self) -> None:
        self.snake: Snake = Snake(GRID_WIDTH // 2, GRID_HEIGHT // 2)
        self.board: Board = Board(GRID_WIDTH, GRID_HEIGHT)
        self.score: int = 0
        self.game_over: bool = False
        self.current_direction: Direction = Direction.RIGHT
        self.next_direction: Direction = Direction.RIGHT


class Game:
    def __init__(self, difficulty: str = "medium") -> None:
        self.difficulty = difficulty
        self.state = GameState()
        self.ui = UI()
        self._running: bool = False

    def start(self) -> None:
        self._running = True
        self.ui.show_instructions()
        
        while self._running and not self.state.game_over:
            self.update()
            self.ui.render({
                "snake": self.state.snake,
                "food": self.state.board.food_position,
                "score": self.state.score,
                "game_over": self.state.game_over
            })
            time.sleep(self.get_difficulty_speed() / 1000.0)

        self.ui.show_game_over(self.state.score)
        self.ui.cleanup()

    def handle_input(self, key: str) -> None:
        if key in ("w", "W", "\x1b[A"):
            new_dir = Direction.UP
        elif key in ("s", "S", "\x1b[B"):
            new_dir = Direction.DOWN
        elif key in ("a", "A", "\x1b[D"):
            new_dir = Direction.LEFT
        elif key in ("d", "D", "\x1b[C"):
            new_dir = Direction.RIGHT
        else:
            return

        if opposite(new_dir) != self.state.current_direction:
            self.state.next_direction = new_dir

    def update(self) -> bool:
        self.state.current_direction = self.state.next_direction
        head_x, head_y = self.state.snake.get_head()

        self.state.snake.move(self.state.current_direction)

        if self.state.snake.check_self_collision():
            self.state.game_over = True
            self._running = False
            return True

        if not self.state.board.is_valid_position(head_x, head_y):
            self.state.game_over = True
            self._running = False
            return True

        if self.state.board.food_at(head_x, head_y):
            self.state.snake.grow()
            self.state.board.remove_food(head_x, head_y)
            self.state.score += 1

        return False

    def get_score(self) -> int:
        return self.state.score

    def get_difficulty_speed(self) -> int:
        return DIFFICULTY_SPEEDS.get(self.difficulty, 150)
