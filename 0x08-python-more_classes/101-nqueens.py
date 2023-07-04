#!/usr/bin/python3
""" N queens puzzle """
import sys


def place_queen(brd, rw, cl):
    """ If queen can be placed on board without attacking other queens """
    for i in range(cl):
        if brd[rw][i] == 1:
            return False

    for i, j in zip(range(rw, -1, -1), range(cl, -1, -1)):
        if brd[i][j] == 1:
            return False

    for i, j in zip(range(rw, len(brd)), range(cl, -1, -1)):
        if brd[i][j] == 1:
            return False

    return True


def nqueens_puzzle(n):
    """ Solve nqueens puzzle """
    def back_tracking(brd, cl, results):
        if cl == n:
            result = []
            for rw in range(n):
                for i in range(n):
                    if brd[rw][i] == 1:
                        result.append([rw, i])
            results.append(result)
        else:
            for rw in range(n):
                if place_queen(brd, rw, cl):
                    brd[rw][cl] = 1
                    back_tracking(brd, cl + 1, results)
                    brd[rw][cl] = 0
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    brd = [[0] * n for i in range(n)]
    results = []
    back_tracking(brd, 0, results)

    for result in results:
        print(result)
        print()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

nqueens_puzzle(N)
