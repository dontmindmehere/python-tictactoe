from random import choice
from time import sleep

class Board:
    def __init__(self):
        self.arr = ([' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' '])
        self.TurnCount = 0


    def validateMove(self, x, y):
        if self.arr[x][y] == ' ':
            return True
        return False

    def setBoardTileAndIncreaseTurnCount(self, x, y):
        self.arr[x][y] = Player.currentPlayer.symbol
        self.TurnCount += 1


    def draw(self):
        print("\n  0   1   2")
        for y in range(3):
            output = []
            for x in range(3):
                item = self.arr[y][x]
                output.append(item)

            print(f"{y} {output[0]} | {output[1]} | {output[2]}")
            if y == 0:
                print("  — — — — —")
            if y == 1:
                print(F"  — — — — —         Current player is {Player.currentPlayer.symbol}")


    def winCondition(self):
        if self.arr[0][0] != ' ' and self.arr[0][0] == self.arr[1][1] and self.arr[1][1] == self.arr[2][2]:
            return True
        if self.arr[0][2] != ' ' and self.arr[0][2] == self.arr[1][1] and self.arr[1][1] == self.arr[2][0]:
            return True
        for row in self.arr:
            if row[0] != ' ' and row[0] == row[1] and row[1] == row[2]:
                return True
        for i in range(3):
            if self.arr[0][i] != ' ' and self.arr[0][i] == self.arr[1][i] and self.arr[1][i] == self.arr[2][i]:
                return True
        return False


    def drawCondition(self):
        if self.TurnCount == 9:
            return True
        return False


class Player:
    players = [None]
    currentPlayer = None

    def __init__(self, symbol):
        self.symbol = symbol
        Player.players.append(self)


    def getInputXY(self):
        while True:
            userinput = input(F"\n{self.symbol} player, Enter the xy spot you wish to play: ")
            #userparsed = []

            #for char in [char for char in userinput if char.isnumeric()]:
            #   userparsed.append(int(char))
            userparsed = [int(char) for char in userinput if char.isnumeric()]

            x, y = int(userparsed[1]), int(userparsed[0])

            if x > 2 or y > 2:
                continue
            return x, y


    @classmethod
    def swapCurrentPlayer(cls):
        index = cls.players.index(cls.currentPlayer)
        cls.currentPlayer = cls.players[index * -1]

    @classmethod
    def setRandomFirstPlayer(cls):
        cls.currentPlayer = cls.players[choice((-1, 1))]


def main():
    board = Board()
    player1 = Player("X")
    player2 = Player("O")

    Player.setRandomFirstPlayer()
    print("Simple Tic Tac Toe. Columns ||| are x, Rows ☰ are y.\n")
    board.draw()



    run = True
    while run:

        while True:
            x, y = Player.currentPlayer.getInputXY()

            if not board.validateMove(x, y):
                print("Invalid move. Try again.")
                continue
            else:
                board.setBoardTileAndIncreaseTurnCount(x, y)
                break


        if board.winCondition():
            board.draw()
            run = False
            print(F"\n{Player.currentPlayer.symbol} wins.\n\n")
            break


        if board.drawCondition():
            board.draw()
            run = False
            print("\nDraw! Restarting..\n\n")
            break


        Player.swapCurrentPlayer()
        board.draw()


if __name__ == "__main__":
    while True:
        main()
        sleep(2)
