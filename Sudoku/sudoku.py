from random import sample
from typing import Optional, Tuple, List

BASE = 3
SIDE = BASE * BASE


def pattern(r: int, c: int) -> int:
    return (BASE * (r % BASE) + r // BASE + c) % SIDE


def shuffle(seq):
    return sample(seq, len(seq))


def generate_full_board() -> List[List[int]]:
    r_base = range(BASE)
    rows = [g * BASE + r for g in shuffle(r_base) for r in shuffle(r_base)]
    cols = [g * BASE + c for g in shuffle(r_base) for c in shuffle(r_base)]
    nums = shuffle(list(range(1, SIDE + 1)))
    return [[nums[pattern(r, c)] for c in cols] for r in rows]


def make_puzzle(board: List[List[int]], empties_ratio: float = 0.75) -> None:
    squares = SIDE * SIDE
    empties = int(squares * empties_ratio)
    for p in sample(range(squares), empties):
        board[p // SIDE][p % SIDE] = 0


def find_empty(board: List[List[int]]) -> Optional[Tuple[int, int]]:
    for r in range(SIDE):
        for c in range(SIDE):
            if board[r][c] == 0:
                return r, c
    return None


def is_valid(board: List[List[int]], n: int, pos: Tuple[int, int]) -> bool:
    r, c = pos

    # Row
    for j in range(SIDE):
        if board[r][j] == n and j != c:
            return False

    # Column
    for i in range(SIDE):
        if board[i][c] == n and i != r:
            return False

    # Box
    box_x = c // BASE
    box_y = r // BASE
    for i in range(box_y * BASE, box_y * BASE + BASE):
        for j in range(box_x * BASE, box_x * BASE + BASE):
            if board[i][j] == n and (i, j) != (r, c):
                return False

    return True


def solve(board: List[List[int]]) -> bool:
    empty = find_empty(board)
    if not empty:
        return True

    r, c = empty
    for n in range(1, SIDE + 1):
        if is_valid(board, n, (r, c)):
            board[r][c] = n
            if solve(board):
                return True
            board[r][c] = 0

    return False


def print_board(board: List[List[int]]) -> None:
    for i in range(SIDE):
        if i % BASE == 0 and i != 0:
            print("-" * 23)
        for j in range(SIDE):
            if j % BASE == 0 and j != 0:
                print("|", end=" ")
            val = board[i][j]
            print(val if val != 0 else ".", end=" ")
        print()


def main() -> None:
    board = generate_full_board()
    make_puzzle(board, empties_ratio=0.75)

    print("Generating the problem...\n")
    print("Your problem is:")
    print_board(board)

    solved = solve(board)

    print("\nSolving the problem...\n")
    if solved:
        print("This is the answer:")
        print_board(board)
    else:
        print("No solution found (unexpected for this generator).")


if __name__ == "__main__":
    main()
