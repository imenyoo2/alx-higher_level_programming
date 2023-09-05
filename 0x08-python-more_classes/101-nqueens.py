#!/usr/bin/python3
import sys


class Board:
    def __init__(self, size):
        self.size = size
        self.__setup_array()

    @property
    def size(self):
        """getter function for __size"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            print("N must be a number")
            sys.exit(1)
        elif value < 4:
            print("N must be at least 4")
            sys.exit(1)
        else:
            self.__size = value

    def __setup_array(self):
        self.__array = []
        for _ in range(self.size):
            self.__array.append([0 for _ in range(self.size)])

    def set_coord(self, row, col):
        self.__array[row][col] = 1

    def unset_coord(self, row, col):
        self.__array[row][col] = 0

    def check_colision_at(self, row, col):

        for i in range(self.size):
            if (self.__array[i][col] and i != row):
                return False

        for i in range(self.size):
            if (self.__array[row][i] and i != col):
                return False

        i = 1
        while row - i >= 0 and col - i >= 0:
            if self.__array[row - i][col - i] == 1:
                return False
            i = i + 1
        i = 1
        while row + i < self.size and col - i >= 0:
            if self.__array[row + i][col - i] == 1:
                return False
            i = i + 1

        return True

    def print_board(self):
        for i in self.__array:
            print(i)

    def print_arr(self):
        arr = []
        buffer = []
        for i in range(0, self.size):
            buffer.append(i)
            for j in range(0, self.size):
                if self.__array[i][j] == 1:
                    buffer.append(j)
                    break
            arr.append(buffer)
            buffer = []
        print(arr)


def print_comb(board, col):
    for row in range(0, size):
        board.set_coord(row, col)
        if board.check_colision_at(row, col):

            if col + 1 != size:
                print_comb(board, col + 1)
                board.unset_coord(row, col)
            else:
                board.print_arr()
                # board.print_board()
                board.unset_coord(row, col)
        else:
            board.unset_coord(row, col)


argv = sys.argv
if len(argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)
elif not argv[1].isnumeric():
    print("N must be a number")
    sys.exit(1)
elif int(argv[1]) < 4:
    print("N must be at least 4")
    sys.exit(1)

size = int(argv[1])
board = Board(size)
print_comb(board, 0)

# TODO: add current position to class
