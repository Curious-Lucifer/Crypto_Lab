import os, sys
from Crypto.Cipher import AES

from secret import FLAG

key = os.urandom(32)

def pad(m):
    padlen = -len(m) % 16
    return m + bytes([0] * padlen)

def main():
    aes = AES.new(key, AES.MODE_ECB)
    
    while True:
        msg = bytes.fromhex(input('msg > ').strip())
        cipher = aes.encrypt(pad(msg + FLAG))
        print(f'cipher = {cipher.hex()}')

try:
    main()
except:
    sys.exit()