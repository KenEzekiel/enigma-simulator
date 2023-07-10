from rotor import rotor
from file_writer import write, write_out

class rotor_controller:
    rotor_one: rotor
    rotor_two: rotor
    rotor_three: rotor
    cnt_1 : int
    cnt_2 : int
    cnt_3 : int
    to_1 : int
    to_2 : int
    to_3 : int

    def __init__(self, wiring_1, wiring_2, wiring_3, cnt_1, cnt_2, cnt_3, to_1, to_2, to_3):
        self.rotor_one = rotor(wiring_1)
        self.rotor_two = rotor(wiring_2)
        self.rotor_three = rotor(wiring_3)
        self.cnt_1 = cnt_1
        self.cnt_2 = cnt_2
        self.cnt_3 = cnt_3
        self.to_1 = to_1
        self.to_2 = to_2
        self.to_3 = to_3
        for i in range(cnt_1):
            self.rotor_one.rotate_left()
        for i in range(cnt_2):
            self.rotor_two.rotate_left()
        for i in range(cnt_3):
            self.rotor_three.rotate_left()


    def rotate(self):
        self.cnt_1 += 1
        self.cnt_1 %= 26
        self.rotor_one.rotate_left()
        if self.cnt_1 == self.to_1:
            self.cnt_2 += 1
            self.cnt_2 %= 26
            self.rotor_two.rotate_left()
            if self.cnt_2 == self.to_2:
                self.cnt_3 += 1
                self.cnt_3 %= 26
                self.rotor_three.rotate_left()


    def rev_rotate(self):
        self.cnt_1 -= 1
        self.cnt_1 %= 26
        self.rotor_one.rotate_right()
        if self.cnt_1 == self.to_1:
            self.cnt_2 -= 1
            self.cnt_2 %= 26
            self.rotor_two.rotate_right()
            if self.cnt_2 == self.to_2:
                self.cnt_3 -= 1
                self.cnt_3 %= 26
                self.rotor_three.rotate_right()


    def substitute_in(self, char):
        out1 = self.rotor_one.get(char)
        write(f"rotor 1 {char} to {out1}")
        write_out(f" -> (R1) {out1}")
        out2 = self.rotor_two.get(out1)
        write(f"rotor 2 {out1} to {out2}")
        write_out(f" -> (R2) {out2}")
        out3 = self.rotor_three.get(out2)
        write(f"rotor 3 {out2} to {out3}")
        write_out(f" -> (R3) {out3}")
        return out3

    def substitute_out(self, char):
        out3 = self.rotor_three.get(char)
        write(f"rotor 3 {char} to {out3}")
        write_out(f" -> (R3) {out3}")
        out2 = self.rotor_two.get(out3)
        write(f"rotor 2 {out3} to {out2}")
        write_out(f" -> (R2) {out2}")
        out1 = self.rotor_one.get(out2)
        write(f"rotor 1 {out2} to {out1}")
        write_out(f" -> (R1) {out1}")
        return out1
    
    def inverse_substitute_in(self, char):
        out1 = self.rotor_one.inverse_get(char)
        write(f"inverse rotor 1 {char} to {out1}")
        write_out(f" -> (IR1) {out1}")
        out2 = self.rotor_two.inverse_get(out1)
        write(f"inverse rotor 2 {out1} to {out2}")
        write_out(f" -> (IR2) {out2}")
        out3 = self.rotor_three.inverse_get(out2)
        write(f"inverse rotor 3 {out2} to {out3}")
        write_out(f" -> (IR3) {out3}")
        return out3

    def inverse_substitute_out(self, char):
        out3 = self.rotor_three.inverse_get(char)
        write(f"inverse rotor 3 {char} to {out3}")
        write_out(f" -> (IR3) {out3}")
        out2 = self.rotor_two.inverse_get(out3)
        write(f"inverse rotor 2 {out3} to {out2}")
        write_out(f" -> (IR2) {out2}")
        out1 = self.rotor_one.inverse_get(out2)
        write(f"inverse rotor 1 {out2} to {out1}")
        write_out(f" -> (IR1) {out1}")
        return out1