from enum import Enum


class Direction(Enum):
    """Cardinal directions for snake movement."""
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


def rotate_left(dir: Direction) -> Direction:
    """Rotate direction 90 degrees counter-clockwise.

    Args:
        dir: The current direction.

    Returns:
        The new direction after left rotation.
    """
    rotation_map = {
        Direction.UP: Direction.RIGHT,
        Direction.RIGHT: Direction.DOWN,
        Direction.DOWN: Direction.LEFT,
        Direction.LEFT: Direction.UP,
    }
    return rotation_map[dir]


def rotate_right(dir: Direction) -> Direction:
    """Rotate direction 90 degrees clockwise.

    Args:
        dir: The current direction.

    Returns:
        The new direction after right rotation.
    """
    rotation_map = {
        Direction.UP: Direction.LEFT,
        Direction.LEFT: Direction.DOWN,
        Direction.DOWN: Direction.RIGHT,
        Direction.RIGHT: Direction.UP,
    }
    return rotation_map[dir]


def opposite(dir: Direction) -> Direction:
    """Return the opposite direction (180 degree turn).

    Args:
        dir: The current direction.

    Returns:
        The opposite direction.
    """
    opposite_map = {
        Direction.UP: Direction.DOWN,
        Direction.DOWN: Direction.UP,
        Direction.LEFT: Direction.RIGHT,
        Direction.RIGHT: Direction.LEFT,
    }
    return opposite_map[dir]
