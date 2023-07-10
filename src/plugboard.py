from string import ascii_uppercase as alc
from file_writer import write, write_out

class plugboard:
    board: dict

    def __init__(self):
        self.board = {}
        for i in alc:
            self.board[i] = i

    def add(self, a, b):
        if (self.board[a] == a and self.board[b] == b):
            self.board[a] = b
            self.board[b] = a
            write(f"Plugged in {a} to {b}")
        else:
            write("Alphabet already plugged in")
    
    def delete(self, x):
        y = self.board[x]
        self.board[x] = x
        self.board[y] = y
        write(f"Unplugged {x}")

    def get(self, x):
        write(f"Plugboard get {x} to {self.board[x]}")
        write_out(f" -> (PB) {self.board[x]}")
        return self.board[x]

    def print(self):
        print(self.board)



# board = plugboard()
# board.add("B", "C")
# board.print()
