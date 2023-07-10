class rotor:
    wiring : dict
    keys: list

    def __init__(self, wiring):
        self.wiring = wiring
        self.keys = []
        for i in self.wiring.keys():
            self.keys.append(i)

    def rotate_left(self):
        # Up
        # print("rotating left")
        first = self.wiring[self.keys[0]]
        for i in range(len(self.keys)-1):
            self.wiring[self.keys[i]] = self.wiring[self.keys[i+1]]
        self.wiring[self.keys[len(self.keys)-1]] = first
        

    def rotate_right(self):
        # Down
        # print("rotating right")
        last = self.wiring[self.keys[len(self.keys)-1]]
        for i in range(len(self.keys)-1, 0, -1):
            self.wiring[self.keys[i]] = self.wiring[self.keys[i-1]]
        self.wiring[self.keys[0]] = last

    def print(self):
        for i in self.wiring.keys():
            print(i, ": ", self.wiring[i])

    def get(self, char):
        return self.wiring[char]
    
    def inverse_get(self, char):
        for i in self.keys:
            if self.wiring[i] == char:
                return i

# wiring = {
#         'A': 'Y',
#         'B': 'R',
#         'C': 'U',
#         'D': 'H',
#         'E': 'Q',
#         'F': 'S',
#         'G': 'L',
#         'H': 'D',
#         'I': 'P',
#         'J': 'X',
#         'K': 'N',
#         'L': 'G',
#         'M': 'O',
#         'N': 'K',
#         'O': 'M',
#         'P': 'I',
#         'Q': 'E',
#         'R': 'B',
#         'S': 'F',
#         'T': 'Z',
#         'U': 'C',
#         'V': 'W',
#         'W': 'V',
#         'X': 'J',
#         'Y': 'A',
#         'Z': 'T'
#     }
# rotor_one = rotor(wiring)
# rotor_one.rotate_left()
# rotor_one.rotate_left()
# rotor_one.rotate_left()
# rotor_one.rotate_left()
# rotor_one.rotate_left()
# rotor_one.rotate_left()
# rotor_one.rotate_right()
# rotor_one.rotate_right()
# rotor_one.rotate_right()
# rotor_one.rotate_right()
# rotor_one.rotate_right()
# rotor_one.rotate_right()
# rotor_one.print()