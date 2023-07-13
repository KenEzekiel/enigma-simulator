from string import ascii_uppercase as alc
class rotor:
    wiring : list
    offset : int

    def __init__(self, wiring, start, offset):
        self.wiring = wiring
        self.offset = (offset + start) % 26

    def rotate_left(self):
        # Up
        # print("rotating left")
        # first = self.wiring[self.keys[0]]
        # for i in range(len(self.keys)-1):
        #     self.wiring[self.keys[i]] = self.wiring[self.keys[i+1]]
        # self.wiring[self.keys[len(self.keys)-1]] = first
        self.offset -= 1
        self.offset %= 26
        

    def rotate_right(self):
        # Down
        # print("rotating right")
        # last = self.wiring[self.keys[len(self.keys)-1]]
        # for i in range(len(self.keys)-1, 0, -1):
        #     self.wiring[self.keys[i]] = self.wiring[self.keys[i-1]]
        # self.wiring[self.keys[0]] = last
        self.offset += 1
        self.offset %= 26

    def print(self):
        for i in range(len(self.wiring)):
            print(alc[i], ": ", self.wiring[i])

    def get(self, char):
        idx = alc.index(char)
        print("idx", idx, "offset", self.offset)
        map_char = self.wiring[(idx + self.offset) % 26]
        print(map_char)
        real = (alc.index(map_char) - self.offset) % 26
        return alc[real]
    
    def inverse_get(self, char):
        idx = alc.index(char)
        print("inv idx", idx, "offset", self.offset)
        map_char = alc[(idx + self.offset) % 26]
        print(map_char)
        real = (self.wiring.index(map_char) - self.offset) % 26
        return alc[real]

# wiring = "E K M F L G D Q V Z N T O W Y H X U S P A I B R C J"
# wiring = wiring.split(" ")
# rotor_one = rotor(wiring, 0, 0)
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
# for i in alc:
#     char = i
#     print(char)
#     char = rotor_one.get(char)
#     print(char)
#     char = rotor_one.inverse_get(char)
#     print(char)
#     print("")
# print(rotor_one.inverse_get("C"))
# rotor_one.print()