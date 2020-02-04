from string import ascii_uppercase as alphabet


def codes_table(char):
    table = {
        "A": 11, "B": 21, "C": 31, "D": 41, "E": 51,
        "F": 12, "G": 22, "H": 32, "I": 42, "K": 52,
        "L": 13, "M": 23, "N": 33, "O": 43, "P": 53,
        "Q": 14, "R": 24, "S": 34, "T": 44, "U": 54,
        "V": 15, "W": 25, "X": 35, "Y": 45, "Z": 55, "J": 0,

        11: "A", 21: "B", 31: "C", 41: "D", 51: "E",
        12: "F", 22: "G", 32: "H", 42: "I", 52: "K",
        13: "L", 23: "M", 33: "N", 43: "O", 53: "P",
        14: "Q", 24: "R", 34: "S", 44: "T", 54: "U",
        15: "V", 25: "W", 35: "X", 45: "Y", 55: "Z", 0: "J"
    }

    return table[char]


def encoding(text):
    text, finished_text = text.upper(), ""
    for symbol in text:
        if symbol in alphabet:
            finished_text += str(codes_table(symbol)) + " "

    return finished_text


def decoding(text):
    text, finished_text = text.upper(), ""
    for symbol in list(map(int, text.split())):
        finished_text += codes_table(symbol)

    return finished_text


def assembly(mode):
    text = str(input("[+] Enter your text - "))

    if mode == 0:
        finished_text = encoding(text)
    else:
        finished_text = decoding(text)

    print("\n »» The result of encoding by Morse algorithm. ««")
    print(finished_text)


def main():
    print("[x] Polybius Square cryptography algorithm. [x]")
    print(" • 0. Encoding mode.\n • 1. Decoding mode.")

    mode = int(input("[?] Select program mode - "))
    assembly(mode)


if __name__ == '__main__':
    main()
