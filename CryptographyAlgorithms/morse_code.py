def codesTable(char):
    table = {
        "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
        "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
        "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
        "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
        "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..",

        ".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E",
        "..-.": "F", "--.": "G", "....": "H", "..": "I", ".---": "J",
        "-.-": "K", ".-..": "L", "--": "M", "-.": "N", "---": "O",
        ".--.": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T",
        "..-": "U", "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y", "--..": "Z",

        "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
        "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",

        "-----": "0", ".----": "1", "..---": "2", "...--": "3", "....-": "4",
        ".....": "5", "-....": "6", "--...": "7", "---..": "8", "----.": "9"
    }

    return table[char]


def encoding(text):
    text, finished_text = text.upper(), ""
    for symbol in text:
        if symbol.isalnum():
            finished_text += codesTable(symbol) + " "

    return finished_text


def decoding(text):
    text, finished_text = text.upper(), ""
    for code in text.split():
        finished_text += codesTable(code)

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
    print("[x] Morse cryptography algorithm. [x]")
    print(" • 0. Encoding mode.\n • 1. Decoding mode.")

    mode = int(input("[?] Select program mode - "))
    assembly(mode)


if __name__ == '__main__':
    main()
