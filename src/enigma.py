from plugboard import plugboard
from rotor import rotor
from rotor_controller import rotor_controller
from ukw_b import ukw_b 
from config import read_config

# Keyboard -> Plugboard -> ETW -> Rotor -> Reflektor -> Rotor -> Plugboard -> Lampboard

class enigma:
    pb : plugboard
    rc : rotor_controller
    rf : ukw_b
    # ETW maps A to A, so not necessary to be shown here (skip step)

    def __init__(self, txt):
        self.pb = plugboard()
        wiring_1, wiring_2, wiring_3, cnt_1, cnt_2, cnt_3, to_1, to_2, to_3 = read_config(txt)
        self.rc = rotor_controller(wiring_1, wiring_2, wiring_3, cnt_1, cnt_2, cnt_3, to_1, to_2, to_3)
        self.rf = ukw_b()

    def plug(self, a, b):
        self.pb.add(a, b)
    
    def unplug(self, x):
        self.pb.delete(x)

    def encrypt(self, char):
        # ETW is skipped
        print("----------ENCRYPT----------")
        print("Input:", char)
        out = self.pb.get(char)
        self.rc.rotate()
        out = self.rc.substitute_in(out)
        out = self.rf.get(out)
        out = self.rc.substitute_out(out)
        out = self.pb.get(out)
        print("Output:", out)
        return out

    def decrypt_rev(self, char):
        print("----------DECRYPT REV----------")
        print("Input:", char)
        out = self.pb.get(char)
        out = self.rc.inverse_substitute_in(out)
        out = self.rf.get(out)
        out = self.rc.inverse_substitute_out(out)
        self.rc.rev_rotate()
        out = self.pb.get(out)
        print("Output:", out)
        return out
    
    def decrypt(self, char):
        print("----------DECRYPT----------")
        print("Input:", char)
        out = self.pb.get(char)
        self.rc.rotate()
        out = self.rc.inverse_substitute_in(out)
        out = self.rf.get(out)
        out = self.rc.inverse_substitute_out(out)
        out = self.pb.get(out)
        print("Output:", out)
        return out
    
    def encrypt_all(self, string):
        out = ""
        for i in string:
            out += self.encrypt(i)
        return out
    
    def decrypt_all_rev(self, string):
        # Has to be reversed first, as rotor needs to be from the last encrypted alphabet
        string = string[::-1]
        out = ""
        for i in string:
            out += self.decrypt_rev(i)
        return out
    
    def decrypt_all(self, string):
        out = ""
        for i in string:
            out += self.decrypt(i)
        return out

eng = enigma("./txt/test.txt")
# a = eng.encrypt_all("ABCDEFGHI")
# print(a)
# print("ROTOR ONE")
# eng.rc.rotor_one.print()
# print("ROTOR TWO")
# eng.rc.rotor_two.print()
# print("ROTOR THREE")
# eng.rc.rotor_three.print()
# a = a[::-1]
# for i in a:
#     print(eng.decrypt(i))
#     print("ROTOR ONE")
#     eng.rc.rotor_one.print()
#     print("ROTOR TWO")
#     eng.rc.rotor_two.print()
#     print("ROTOR THREE")
#     eng.rc.rotor_three.print()
b = eng.decrypt_all("CAVSISDMM")
# b = b[::-1]
print(b)
# eng.rc.rotor_one.print()
