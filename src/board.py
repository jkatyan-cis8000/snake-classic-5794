from typing import Tuple, List
from config import GRID_WIDTH, GRID_HEIGHT
import random


class Board:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.food_position: Tuple[int, int] = self.place_food()

    def place_food(self) -> Tuple[int, int]:
        x = random.randint(0, self.width - 1)
        y = random.randint(0, self.height - 1)
        self.food_position = (x, y)
        return (x, y)

    def is_valid_position(self, x: int, y: int) -> bool:
        return 0 <= x < self.width and 0 <= y < self.height

    def is_self_collision(self, x: int, y: int, snake_body: List[Tuple[int, int]]) -> bool:
        return (x, y) in snake_body

    def food_at(self, x: int, y: int) -> bool:
        return self.food_position == (x, y)

    def remove_food(self, x: int, y: int) -> None:
        if self.food_at(x, y):
            self.food_position = self.place_food()
