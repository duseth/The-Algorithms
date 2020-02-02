def processing(mode, text, key):
    key_ints = [ord(i) for i in key]
    text_ints = [ord(i) for i in text]
    finished_text = ""
    for i in range(len(text_ints)):
        adder = key_ints[i % len(key)]
        if mode == 1:
            adder *= -1
        char = (text_ints[i] - 32 + adder) % 95
        finished_text += chr(char + 32)
    return finished_text


def assembly(mode):
    text = str(input("[+] Enter your text - "))
    key = str(input("[+] Enter your key - "))

    finished_text = processing(mode, text, key)

    print("\n »» The result by Vigenere algorithm. ««")
    print(finished_text)


def main():
    print("[x] Vigenere cryptography algorithm. [x]")
    print(" • 0. Encryption mode.\n • 1. Decryption mode.")

    mode = int(input("[?] Select program mode - "))
    assembly(mode)


if __name__ == '__main__':
    main()
