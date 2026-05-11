import argparse
import sys

from game import Game


VALID_DIFFICULTIES = ("easy", "medium", "hard")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Classic Snake Game")
    parser.add_argument(
        "--difficulty",
        choices=VALID_DIFFICULTIES,
        default="medium",
        help="Game difficulty level (default: medium)",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    try:
        game = Game(args.difficulty)
        game.start()
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
