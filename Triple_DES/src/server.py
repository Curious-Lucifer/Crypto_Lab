import os
import sys

from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad

from secret import FLAG

xor = lambda x, y: bytes(i ^ j for i, j in zip(x, y))
iv = os.urandom(len(pad(FLAG.encode(), 8)))


def encrypt(plaintext):
    key = bytes.fromhex(input("> Input Key: "))
    plaintext = xor(pad(plaintext, 8), iv)
    cipher = DES3.new(key, DES3.MODE_ECB)
    ciphertext = cipher.encrypt(plaintext)
    ciphertext = xor(ciphertext, iv)
    print(f"ciphertext: {ciphertext.hex()}")


def main():
    while True:
        print("> encrypt")
        print("> encrypt_flag")
        print("> server.py")
        print("> exit")
        cmd = input("> Command: ")
        if cmd == "exit":
            sys.exit()
        elif cmd == "encrypt":
            encrypt(bytes.fromhex(input("> Input Plaintext: ")))
        elif cmd == "encrypt_flag":
            encrypt(FLAG.encode())
        elif cmd == "server.py":
            print(open("./server.py", "r").read())
        else:
            print("Bad hacker")


if __name__ == "__main__":
    try:
        main()
    except:
        sys.exit()