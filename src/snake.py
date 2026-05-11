from typing import List, Tuple

from direction import Direction


class Snake:
    """Snake class for the classic Snake game."""

    def __init__(self, start_x: int, start_y: int) -> None:
        """Initialize snake with head position.

        Args:
            start_x: Initial x coordinate of head.
            start_y: Initial y coordinate of head.
        """
        self._body: List[Tuple[int, int]] = [(start_x, start_y)]
        self._grow_next_move: bool = False

    def get_head(self) -> Tuple[int, int]:
        """Return current head position."""
        return self._body[0]

    def get_body(self) -> List[Tuple[int, int]]:
        """Return all body segments from head to tail."""
        return list(self._body)

    def move(self, direction: Direction) -> None:
        """Advance snake one cell in given direction.

        Args:
            direction: Direction to move (UP, DOWN, LEFT, RIGHT).
        """
        head_x, head_y = self._body[0]

        if direction == Direction.UP:
            new_head = (head_x, head_y - 1)
        elif direction == Direction.DOWN:
            new_head = (head_x, head_y + 1)
        elif direction == Direction.LEFT:
            new_head = (head_x - 1, head_y)
        elif direction == Direction.RIGHT:
            new_head = (head_x + 1, head_y)

        self._body.insert(0, new_head)

        if not self._grow_next_move:
            self._body.pop()
        else:
            self._grow_next_move = False

    def grow(self) -> None:
        """Extend body on eating food."""
        self._grow_next_move = True

    def check_self_collision(self) -> bool:
        """Check if head collides with any body segment."""
        head = self._body[0]
        return head in self._body[1:]
