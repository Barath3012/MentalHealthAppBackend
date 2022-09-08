
import turtle
import copy
import math
from itertools import permutations

turtle.ht()


class MyTurtle(turtle.Turtle):

    def __init__(self):

        super().__init__()
        self.currentTurn = "X"
        self.endy = False
        self.xo = [["-", "-", "-"] for i in range(3)]

        self.ht()
        self._tracer(False)
        self.speed(0)
        self.createcanvas()
        turtle.onscreenclick(self.clickAction)

    def createcanvas(self):

        self.penup()
        self.goto(-350, 350 // 3)
        self.pendown()
        self.fd(700)
        self.penup()
        self.goto(-350, -350 // 3)
        self.pendown()
        self.fd(700)
        self.penup()
        self.penup()
        self.goto(350 // 3, 350)
        self.pendown()
        self.setheading(270)
        self.fd(700)
        self.penup()
        self.goto(-350 // 3, 350)
        self.setheading(270)
        self.pendown()
        self.fd(700)
        self.penup()

    def drawX(self, x, y):
        self.penup()
        self.goto(x, y)
        self.pendown()
        self.write("X", font=("Arial", 130, "normal"))

    def drawO(self, x, y):
        self.penup()
        self.goto(x, y)
        self.pendown()
        self.write("O", font=("Arial", 130, "normal"))

    def xwins(self):
        self.reset()
        self.goto(-250, -50)
        self.write("X WINS!", font=("Arial", 100, "normal"))
        self.endy = True

    def owins(self):
        self.reset()
        self.goto(-250, -50)
        self.write("O WINS!", font=("Arial", 100, "normal"))
        self.endy = True

    def draw(self):
        self.reset()
        self.goto(-250, -50)
        self.write("DRAW!", font=("Arial", 100, "normal"))
        self.endy = True

    def check(self):
        b = ""
        for i in self.xo:
            a = ""
            for j in i:
                a += str(j)
                b += j
            if a == "XXX":
                self.xwins()
                return 1

            elif a == "OOO":
                self.owins()
                return 1
        if "-" not in b:
            self.draw()

        for i in range(3):
            a = ""
            for j in range(3):
                ele = self.xo[j][i]
                a += ele
            if a == "XXX":
                self.xwins()
                return 1
            elif a == "OOO":
                self.owins()
                return 1
        a = ""
        for i in range(3):

            for j in range(3):
                if i == j:
                    a += self.xo[i][j]
            if a == "XXX":
                self.xwins()
                return 1
            elif a == "OOO":
                self.owins()
                return 1
        a = ""
        for i in range(3):

            for j in range(3):
                if i + j == 2:
                    a += self.xo[i][j]

            if a == "XXX":
                self.xwins()
                return 1
            elif a == "OOO":
                self.owins()
                return 1

        return 0

    def clickAction(self, x, y):
        #AI = xoAI(self.xo,"X")
        #AI.nextMove()
        if self.endy:
            self.reset()
            self.__init__()
            return
        if self.check() == 1:
            print("Yes, you won")
            return
        if x > -350 and x < -350 // 3:
            if y > -350 and y < -350 // 3:
                if self.currentTurn == "X":
                    if self.xo[2][0] == "-":
                        self.xo[2][0] = "X"
                    else:
                        return
                    self.drawX(-300, -325)
                    self.currentTurn = "O"

                else:
                    if self.xo[2][0] == "-":
                        self.xo[2][0] = "O"
                    else:
                        return
                    self.drawO(-300, -325)
                    self.currentTurn = "X"

            elif y >= -350 // 3 and y < 350 // 3:
                if self.currentTurn == "X":
                    if self.xo[1][0] == "-":
                        self.xo[1][0] = "X"
                    else:
                        return
                    self.drawX(-300, -350 // 3 + 25)
                    self.currentTurn = "O"


                else:
                    if self.xo[1][0] == "-":
                        self.xo[1][0] = "O"
                    else:
                        return
                    self.drawO(-300, -350 // 3 + 25)
                    self.currentTurn = "X"


            else:

                if self.currentTurn == "X":
                    if self.xo[0][0] == "-":
                        self.xo[0][0] = "X"
                    else:
                        return
                    self.drawX(-300, 350 // 3)
                    self.currentTurn = "O"


                else:
                    if self.xo[0][0] == "-":
                        self.xo[0][0] = "O"
                    else:
                        return
                    self.drawO(-300, 350 // 3)
                    self.currentTurn = "X"

        elif x > 350 // 3 and x < 350:
            if y > -350 and y < -350 // 3:
                if self.currentTurn == "X":
                    if self.xo[2][2] == "-":
                        self.xo[2][2] = "X"
                    else:
                        return
                    self.drawX(300 // 3 + 50, -325)
                    self.currentTurn = "O"
                else:
                    if self.xo[2][2] == "-":
                        self.xo[2][2] = "O"
                    else:
                        return
                    self.drawO(300 // 3 + 50, -325)
                    self.currentTurn = "X"
            elif y >= -350 // 3 and y < 350 // 3:
                if self.currentTurn == "X":
                    if self.xo[1][2] == "-":
                        self.xo[1][2] = "X"
                    else:
                        return
                    self.drawX(300 // 3 + 50, -350 // 3 + 25)
                    self.currentTurn = "O"
                else:
                    if self.xo[1][2] == "-":
                        self.xo[1][2] = "O"
                    else:
                        return
                    self.drawO(300 // 3 + 50, -350 // 3 + 25)
                    self.currentTurn = "X"

            else:

                if self.currentTurn == "X":
                    if self.xo[0][2] == "-":
                        self.xo[0][2] = "X"
                    else:
                        return
                    self.drawX(300 // 3 + 50, 350 // 3)
                    self.currentTurn = "O"
                else:
                    if self.xo[0][2] == "-":
                        self.xo[0][2] = "O"
                    else:
                        return
                    self.drawO(300 // 3 + 50, 350 // 3)
                    self.currentTurn = "X"
        elif x < 350 // 3 and x > -350 // 3:
            if y > -350 and y < -350 // 3:
                if self.currentTurn == "X":
                    if self.xo[2][1] == "-":
                        self.xo[2][1] = "X"
                    else:
                        return
                    self.drawX(-300 // 3 + 35, -325)
                    self.currentTurn = "O"
                else:
                    if self.xo[2][1] == "-":
                        self.xo[2][1] = "O"
                    else:
                        return
                    self.drawO(-300 // 3 + 35, -325)
                    self.currentTurn = "X"
            elif y >= -350 // 3 and y < 350 // 3:
                if self.currentTurn == "X":
                    if self.xo[1][1] == "-":
                        self.xo[1][1] = "X"
                    else:
                        return
                    self.drawX(-300 // 3 + 35, -350 // 3 + 25)
                    self.currentTurn = "O"
                else:
                    if self.xo[1][1] == "-":
                        self.xo[1][1] = "O"
                    else:
                        return
                    self.drawO(-300 // 3 + 35, -350 // 3 + 25)
                    self.currentTurn = "X"

            else:

                if self.currentTurn == "X":
                    if self.xo[0][1] == "-":
                        self.xo[0][1] = "X"
                    else:
                        return

                    self.drawX(-300 // 3 + 35, 350 // 3)
                    self.currentTurn = "O"
                else:
                    if self.xo[0][1] == "-":
                        self.xo[0][1] = "O"
                    else:
                        return
                    self.drawO(-300 // 3 + 35, 350 // 3)
                    self.currentTurn = "X"


class xoAI(object):
    def __init__(self, moves, symbol):
        self.moves = moves
        self.symbol = symbol

    def nextMove(self):

        self.availableMoves = self.AvailableMoves(self.moves)
        print(self.FindBestMove(self.availableMoves))

    def AvailableMoves(self, moves):
        nono = []
        for i in range(len(moves)):
            for j in range(len(moves[i])):
                if moves[i][j] == "-":
                    nono.append(str(i) + str(j))

        return nono

    def givePermutationThingy(self, length):
        listo = [i for i in range(1, length + 1)]
        return list(permutations(listo))

    def FindBestMove(self, moveList):
        evaMove = {}
        print(moveList)
        for i in moveList:
            evaMove[i] = self.WorL(self.moves,i,moveList)
        # higest = evaMove[list(evaMove.values())[0]][0]
        higest = 0
        item = None
        for j in evaMove:
            print(higest,evaMove[j][0],evaMove,evaMove[j])
            if higest < evaMove[j][0]:
                higest = evaMove[j][0]
                item = j
        if item == None:
            raise Exception("YOU MESSED UP HASHAHAHAHAHAHA")
        return item

    def WorL(self, moves, move, moveList):

        Moves = copy.deepcopy(moves)
        print(Moves[int(move[0])][int(move[1])])
        Moves[int(move[0])][int(move[1])] = self.symbol
        MoveList = copy.deepcopy(moveList)
        MoveList.remove(move)
        WCount = 0
        DCount = 0
        AllCombinations = self.givePermutationThingy(len(MoveList))
        i=0
        while i < len(AllCombinations):
            ThisCombination = AllCombinations[i]
            j = 0
            while len(MoveList)-1 > j:
                #print(MoveList,ThisCombination,j)
                nextMove = MoveList[ThisCombination[j]-1]
                if self.symbol == "X":
                    Moves[int(move[0])][int(move[1])] = "O"
                else:
                    Moves[int(move[0])][int(move[1])] = "X"
                meow = self.check(Moves)
                if meow == 0:
                    pass
                elif meow == 2:
                    DCount += 1
                    break
                else:
                    WCount += 1
                    break

                j += 1
            i+=1
        return WCount, DCount

    def check(self, moves):
        b = ""
        for i in moves:
            a = ""
            for j in i:
                a += str(j)
                b += j
            if a == "XXX":

                return 1

            elif a == "OOO":

                return 1
        if "-" not in b:
            return 2

        for i in range(3):
            a = ""
            for j in range(3):
                ele = moves[j][i]
                a += ele
            if a == "XXX":

                return 1
            elif a == "OOO":

                return 1
        a = ""
        for i in range(3):

            for j in range(3):
                if i == j:
                    a += moves[i][j]
            if a == "XXX":
                return 1
            elif a == "OOO":

                return 1
        a = ""
        for i in range(3):

            for j in range(3):
                if i + j == 2:
                    a += moves[i][j]

            if a == "XXX":
                return 1
            elif a == "OOO":
                return 1

        return 0


if __name__ == "__main__":
    mythingy = MyTurtle()
    turtle.mainloop()
