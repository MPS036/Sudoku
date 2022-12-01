from random import sample

base = 3
side = base * base


def pattern(r, c):
    return (base * (r % base) + r // base + c) % side


def shuffle(s):
    return sample(s, len(s))


rBase = range(base)
rows = [g * base + r for g in shuffle(rBase) for r in shuffle(rBase)]
cols = [g * base + c for g in shuffle(rBase) for c in shuffle(rBase)]
nums = shuffle(range(1, base * base + 1))

board = [[nums[pattern(r, c)] for c in cols] for r in rows]

squares = side * side
empties = squares * 3 // 4
for p in sample(range(squares), empties):
    board[p // side][p % side] = 0


def solution(b):
    find = find_zero(b)
    if not find:
        return True
    else:
        x, y = find
    for i in range(1, 10):
        if valid(b, i, (x, y)):
            b[x][y] = i
            if solution(b):
                return True
            b[x][y] = 0
    return False


def valid(b, n, p):
    for i in range(len(b[0])):
        if (b[p[0]][i] == n) and (p[1] != i):
            return False
    for i in range(len(b)):
        if (b[i][p[1]] == n) and (p[0] != i):
            return False
    b_x = p[1] // 3
    b_y = p[0] // 3
    for i in range(b_y * 3, b_y * 3 + 3):
        for j in range(b_x * 3, b_x * 3 + 3):
            if (b[i][j] == n) and ((i, j) != p):
                return False
    return True


def set_up_board(b):
    for i in range(len(b)):
        if (i % 3 == 0) and (i != 0):
            print("-----------------------")
        for j in range(len(b[0])):
            if (j % 3 == 0) and (j != 0):
                print(" | ", end = "")
            if j == 8:
                print(b[i][j])
            else:
                print(str(b[i][j]) + " ", end = "")


def find_zero(b):
    for i in range(len(b)):
        for j in range(len(b[0])):
            if b[i][j] == 0:
                return (i, j)
    return None


print("Generating the problem...")
print("Your problem is:")
set_up_board(board)
solution(board)
print("Solving the problem...")
print("This is the answer:")
set_up_board(board)