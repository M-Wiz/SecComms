import string
import random
from base64 import b64encode, b64decode

secret = "112Mk1USmFla1ZWU1dGamVFUkhNRGs9"  # We don't know the original message or length

secret_encoding = ['step1', 'step2', 'step3']
secret_decoding = ['step1', 'decodestep2', 'decodestep3']

def step1(s):
    _step1 = str.maketrans(
        "zyxwvutsrqponZYXWVUTSRQPONmlkjihgfedcbaMLKJIHGFEDCBA",
        "mlkjihgfedcbaMLKJIHGFEDCBAzyxwvutsrqponZYXWVUTSRQPON"
    )
    return s.translate(_step1)

def step2(s): return b64encode(s.encode()).decode()

def decodestep2(s): return b64decode(s).decode()

def step3(plaintext, shift=4):
    loweralpha = string.ascii_lowercase
    shifted_string = loweralpha[shift:] + loweralpha[:shift]
    converted = str.maketrans(loweralpha, shifted_string)
    return plaintext.translate(converted)

def decodestep3(plaintext, shift=-4):
    loweralpha = string.ascii_lowercase
    shifted_string = loweralpha[shift:] + loweralpha[:shift]
    converted = str.maketrans(loweralpha, shifted_string)
    return plaintext.translate(converted)

def decrypt(secret):
    while True:
        count = 0
        try:
            count = int(secret[0])
            r = secret_decoding[count-1]
        except:
            return secret
        secret = secret[1:]
        _secret_text = globals()[r](secret)
        secret = _secret_text

if __name__ == '__main__':
    print(decrypt(secret))