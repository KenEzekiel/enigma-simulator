from file_writer import write,write_out
class ukw_b:
    wiring = {
        'A': 'Y',
        'B': 'R',
        'C': 'U',
        'D': 'H',
        'E': 'Q',
        'F': 'S',
        'G': 'L',
        'H': 'D',
        'I': 'P',
        'J': 'X',
        'K': 'N',
        'L': 'G',
        'M': 'O',
        'N': 'K',
        'O': 'M',
        'P': 'I',
        'Q': 'E',
        'R': 'B',
        'S': 'F',
        'T': 'Z',
        'U': 'C',
        'V': 'W',
        'W': 'V',
        'X': 'J',
        'Y': 'A',
        'Z': 'T'
    }

    def get(self, char):
        write(f"Reflector UKW-B {char} to {self.wiring[char]}")
        write_out(f" -> (R) {self.wiring[char]}")
        return self.wiring[char]