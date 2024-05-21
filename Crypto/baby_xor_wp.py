import binascii
c = 'edafafebadafadabe4e7afedc0f6aac0eeeaaeebacc0acfee5e6e2'

def xor(plaintext, key):
    ret = []
    for i in range(len(plaintext)):
        ret.append(plaintext[i] ^ key[0])
    return bytes(ret)

c = binascii.a2b_hex(c)

for i in range(0, 256):

    key = bytes([i])
    ciphertext = xor(c, key)

    if b'r00t2024' in ciphertext:
        try:
            print(ciphertext.decode())
        except UnicodeDecodeError:
            print("Found 'flag' but cannot decode:", ciphertext)