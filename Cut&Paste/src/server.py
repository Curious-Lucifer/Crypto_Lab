import os, sys, json
from Crypto.Cipher import AES

from secret import FLAG

key = os.urandom(32)

def pad(msg):
    pad = 16 - (len(msg) % 16)
    return msg + bytes([pad]) * pad

def unpad(msg):
    assert 1 <= msg[-1] <= 16
    assert msg.endswith(msg[-1:] * msg[-1])
    return msg[:-msg[-1]]

def encrypt(msg):
    aes = AES.new(key, AES.MODE_ECB)
    return aes.encrypt(pad(msg))

def decrypt(msg):
    aes = AES.new(key, AES.MODE_ECB)
    return unpad(aes.decrypt(msg))

def login():
    user = input('> user : ')
    if 'admin' in user:
        sys.exit()
    data = {'user': user, 'admin': '0'}
    token = encrypt(json.dumps(data))
    print(f'token : {token.hex()}')

def verify():
    token = bytes.fromhex(input('> token : '))
    try:
        data = json.loads(decrypt(token))
    except:
        print('Wrong !')
        sys.exit()
    if int(data['admin']) == 1:
        print(FLAG)
    else:
        print('You are not admin QQ')
    sys.exit()


def main():
    while True:
        print("> login")
        print("> verify")
        print("> server.py")
        print("> exit")
        cmd = input("> Command: ")
        if cmd == "exit":
            sys.exit()
        elif cmd == "login":
            login()
        elif cmd == "verify":
            verify()
        elif cmd == "server.py":
            print(open("./server.py", "r").read())
            sys.exit()
        else:
            print('Wrong command !')
            sys.exit()

try:
    main()
except:
    sys.exit()