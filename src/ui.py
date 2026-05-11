import curses
from typing import Tuple
from config import GRID_WIDTH, GRID_HEIGHT, SNAKE_CHAR, FOOD_CHAR, EMPTY_CHAR
from direction import Direction


class UI:
    def __init__(self) -> None:
        self.stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        self.stdscr.nodelay(True)
        self.stdscr.keypad(True)

    def render(self, game_state: dict) -> None:
        self.stdscr.clear()
        snake = game_state["snake"]
        food = game_state["food"]
        score = game_state["score"]

        board = [[EMPTY_CHAR for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

        for x, y in snake.get_body():
            if 0 <= x < GRID_WIDTH and 0 <= y < GRID_HEIGHT:
                board[y][x] = SNAKE_CHAR

        fx, fy = food
        if 0 <= fx < GRID_WIDTH and 0 <= fy < GRID_HEIGHT:
            board[fy][fx] = FOOD_CHAR

        for y in range(GRID_HEIGHT):
            self.stdscr.addstr(y, 0, "".join(board[y]))

        self.stdscr.addstr(GRID_HEIGHT, 0, f"Score: {score}")
        self.stdscr.refresh()

    def get_user_input(self) -> str:
        try:
            key = self.stdscr.getkey()
            return key
        except curses.error:
            return ""

    def show_game_over(self, score: int) -> None:
        self.stdscr.nodelay(False)
        self.stdscr.clear()
        center_y = GRID_HEIGHT // 2
        game_over_msg = "GAME OVER"
        score_msg = f"Final Score: {score}"
        
        self.stdscr.addstr(center_y - 1, (GRID_WIDTH - len(game_over_msg)) // 2, game_over_msg)
        self.stdscr.addstr(center_y, (GRID_WIDTH - len(score_msg)) // 2, score_msg)
        self.stdscr.addstr(center_y + 2, (GRID_WIDTH - 22) // 2, "Press any key to exit")
        self.stdscr.refresh()
        self.stdscr.getch()

    def show_instructions(self) -> None:
        self.stdscr.nodelay(False)
        self.stdscr.clear()
        instructions = [
            "SNAKE GAME",
            "",
            "Instructions:",
            "- Use Arrow keys or WASD to move",
            "- Eat food (O) to grow and score",
            "- Avoid hitting walls or yourself",
            "",
            "Press any key to start..."
        ]
        
        start_y = (GRID_HEIGHT - len(instructions)) // 2
        for i, line in enumerate(instructions):
            self.stdscr.addstr(start_y + i, (GRID_WIDTH - len(line)) // 2, line)
        
        self.stdscr.refresh()
        self.stdscr.getch()

    def cleanup(self) -> None:
        curses.nocbreak()
        self.stdscr.keypad(False)
        curses.echo()
        curses.endwin()
