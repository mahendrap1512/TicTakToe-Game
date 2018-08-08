class TTTBoard:
    def __init__(self):
        self.board = [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]
        self.moves = 1
    def __str__(self):
        #try(IndexError):
        if self.moves == -1:
            print("| _ _ _ |")
            print("| _ _ _ |")
            print("| _ _ _ |")
        else:
            print("| ",end="")
            for i in range(3):
                if self.board[0][i] != -1:
                    print(self.board[0][i], end=" ")
                else:
                    print("_",end=" ")
            print("|")
            print("| ", end="")
            for i in range(3):
                if self.board[1][i] != -1:
                    print(self.board[1][i], end=" ")
                else:
                    print("_",end=" ")
            print("|")
            print("| ", end="")
            for i in range(3):
                if self.board[2][i] != -1:
                    print(self.board[2][i], end=" ")
                else:
                    print("_",end=" ")
            print("|")
            print()

    def clear_board(self):
        self.board.clear()
    #def check(self,)
    def hasWon(self,player):
        #check rowwise
        for i in range(3):
            if self.board[i][0] == player and self.board[i][1] == player and self.board[i][2] == player:
                print("Player {} Won!".format(player+1))
                return True
        #check cloumnwise
        for i in range(3):
            if self.board[0][i] == player and self.board[1][i] == player and self.board[2][i] == player:
                print("Player {} Won!".format(player+1))
                return  True
        #check digonal
        if self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player:
            print("Player {} Won!".format(player+1))
            return True
        if self.board[0][2] == player and self.board[1][1] == player and self.board[2][0] == player:
            print("Player {} Won!".format(player+1))
            return True
        else:
            return False

    def gameOver(self):
        for i in range(3):
            for j in range(3):
                if self.hasWon(0)== True or self.hasWon(1)==True:
                    return True
                if self.board[i][j] == -1:
                    return False
        return True

    def makeMove(self,player,pos):
        try:
            if self.board[pos[0]][pos[1]] != -1:
                print("Invalid Move!, Try again.")
                return False
            else:
                self.board[pos[0]][pos[1]] = player
                self.__str__()
                return True
        except IndexError:
            print("Invalid Move!, Try again.")
            return False


    def run(self):
        print()
        print("Instructions : ")
        print("Index format is like this: ")
        print("| 00 01 02 |")
        print("| 10 11 12 |")
        print("| 20 21 22 |")
        print("")
        print("Enter \"exit\" to quit the game." )
        print("Your Board look like this : ")
        self.__str__()
        print("Input in this format ab where a is row no b is column no, index are 0 based")
        print("\n")
        while not(self.hasWon(0) == True or self.hasWon(1)== True or self.gameOver()==True):
            while True:
                ipstr = (input("Enter position for first player in row,col : "))
                if ipstr == "exit" or ipstr == "Exit":
                    return
                ip = [-1,-2]
                try:
                    ip[0] = int(ipstr[0])
                    ip[1] = int(ipstr[1])
                    if self.makeMove(0,ip) == True:
                        if self.hasWon(0) == True or self.hasWon(1)== True or self.gameOver()==True:
                            return
                        break
                except ValueError:
                    print("Invalid Instruction")
            while True:
                ipstr2 = (input("Enter position for second player in row,col : "))
                if ipstr2 == "exit" or ipstr2 == "Exit":
                    return
                try:
                    ip2 = [-1,-2]
                    ip2[0] = int(ipstr2[0])
                    ip2[1] = int(ipstr2[1])
                    if self.makeMove(1,ip2) == True:
                        break
                except ValueError:
                    print("Invalid Instruction")



a = TTTBoard()
a.run()
