from string import ascii_uppercase as alc

class plugboard:
    board: dict

    def __init__(self):
        self.board = {}
        for i in alc:
            self.board[i] = i

    def add(self, a, b):
        self.board[a] = b
        self.board[b] = a
    
    def delete(self, x):
        y = self.board[x]
        self.board[x] = x
        self.board[y] = y

    def get(self, x):
        print("Plugboard get", x, "to", self.board[x])
        return self.board[x]

    def print(self):
        print(self.board)



# board = plugboard()
# board.add("B", "C")
# board.print()
