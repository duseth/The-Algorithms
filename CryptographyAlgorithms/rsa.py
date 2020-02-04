"""
 Further in creation_keys() function will be used alphabetic variables.
 I will explain the meaning of each of them.
 They were used for convenience.
 [p], [q] - two prime numbers.
 [n] - the product of [p] on [q].
 [f] - euler function of [n].
 [e] - an open exponent is such that ([e] is prime) and (e < f) and (f mod e != 0).
 [d] - an secret exponent is such that (d * e) mod f = 1.
"""
from math import sqrt
from random import randint


def is_prime(n):
    i = 2
    while i <= sqrt(n):
        if n % i == 0:
            return False
        i += 1
    return True


def creation_keys():
    p, q, e = 10, 10, 4
    while not is_prime(p):
        p = randint(500, 700)
    while not is_prime(q):
        q = randint(500, 700)
    n, f, d = p * q, (p - 1) * (q - 1), 0
    while (not is_prime(e)) or (e > f) or (f % e == 0):
        e += 1
    while (d * e) % f != 1:
        d += 1
    return (e, n), (d, n)


def encoding(text, open_key):
    cipher_list = []
    e, n = open_key
    for letter in text:
        cipher_list.append(ord(letter) ** e % n)

    return cipher_list


def decoding(cipher_list, close_key):
    text = ""
    d, n = close_key
    for item in cipher_list:
        text += chr(int(item) ** d % n)

    return text


def encoding_mode():
    print("\n » Encoding mode activated! « (~˘▾˘)~")

    text = str(input("[+] Enter your text - "))
    open_key, close_key = creation_keys()
    print("[~] Your open key - [{},{}].".format(open_key[0], open_key[1]))
    print("[~] Your close key - [{},{}].".format(close_key[0], close_key[1]))

    cipher_list = encoding(text, open_key)

    print("\n »» The result of encoding by RSA algorithm. ««")
    print(cipher_list)


def decoding_mode():
    print("\n » Decoding mode activated! « (~˘▾˘)~")

    cipher_list = eval(input("[+] Enter your cipher list - "))
    close_key = eval(input("[+] Enter your close key - "))

    text = decoding(cipher_list, close_key)

    print("\n »» The result of decoding by RSA algorithm. ««")
    print(text)


def main():
    print("[x] Rivest–Shamir–Adleman cryptography algorithm. [x]")
    print(" • 0. Encoding mode.\n • 1. Decoding mode.")

    mode = int(input("[?] Select program mode - "))

    if mode == 0:
        encoding_mode()
    elif mode == 1:
        decoding_mode()
    else:
        print("[x] Invalid input! You can only select: \"0, 1, 2\".")
        raise SystemExit


if __name__ == '__main__':
    main()
