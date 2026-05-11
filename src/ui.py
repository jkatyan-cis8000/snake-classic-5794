import curses
from typing import List, Tuple

from config import GRID_WIDTH, GRID_HEIGHT, FOOD_CHAR, SNAKE_CHAR, EMPTY_CHAR
from snake import Snake


class GameState:
    def __init__(self, snake: Snake, food: Tuple[int, int], score: int, game_over: bool) -> None:
        self.snake = snake
        self.food = food
        self.score = score
        self.game_over = game_over


class UI:
    def __init__(self) -> None:
        self._stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        self._stdscr.nodelay(True)
        self._stdscr.keypad(True)

    def render(self, game_state: GameState) -> None:
        self._stdscr.clear()
        
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                head = game_state.snake.get_head()
                body = game_state.snake.get_body()
                if head == (x, y):
                    self._stdscr.addch(y, x, SNAKE_CHAR)
                elif body and (x, y) in body:
                    self._stdscr.addch(y, x, SNAKE_CHAR.lower())
                elif game_state.food == (x, y):
                    self._stdscr.addch(y, x, FOOD_CHAR)
                else:
                    self._stdscr.addch(y, x, EMPTY_CHAR)
        
        self._stdscr.addstr(GRID_HEIGHT + 1, 0, f"Score: {game_state.score}")
        self._stdscr.refresh()

    def get_user_input(self) -> str:
        try:
            key = self._stdscr.getkey()
            return key
        except curses.error:
            return ""

    def show_game_over(self, score: int) -> None:
        self._stdscr.clear()
        self._stdscr.addstr(GRID_HEIGHT // 2, GRID_WIDTH // 2 - 5, "Game Over!")
        self._stdscr.addstr(GRID_HEIGHT // 2 + 1, GRID_WIDTH // 2 - 6, f"Final Score: {score}")
        self._stdscr.addstr(GRID_HEIGHT // 2 + 3, GRID_WIDTH // 2 - 11, "Press any key to exit")
        self._stdscr.refresh()
        self._stdscr.nodelay(False)
        self._stdscr.getkey()

    def show_instructions(self) -> None:
        self._stdscr.clear()
        self._stdscr.addstr(0, 0, "Snake Game Instructions")
        self._stdscr.addstr(2, 0, "Use arrow keys to change direction")
        self._stdscr.addstr(3, 0, "Collect 'O' to grow and score")
        self._stdscr.addstr(4, 0, "Don't hit walls or yourself")
        self._stdscr.addstr(6, 0, "Press any key to start")
        self._stdscr.refresh()
        self._stdscr.nodelay(False)
        self._stdscr.getkey()

    def cleanup(self) -> None:
        curses.nocbreak()
        self._stdscr.keypad(False)
        curses.echo()
        curses.endwin()
