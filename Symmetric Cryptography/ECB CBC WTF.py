from Crypto.Cipher import AES
from pwn import xor
import requests

def get_ciphertext():
    url = "http://aes.cryptohack.org//ecbcbcwtf/encrypt_flag/"
    response = requests.get(url)
    return response.json()['ciphertext']

def decrypt_block(data):
    url = "http://aes.cryptohack.org/ecbcbcwtf/decrypt/"
    response = requests.get(url + data + '/')
    return response.json()['plaintext']

def decrypt_and_xor(ciphertext_block, initialization_vector):
    decrypted_block = decrypt_block(ciphertext_block)
    return xor(bytes.fromhex(decrypted_block), bytes.fromhex(initialization_vector)).decode()

def main():
    encrypted_flag = get_ciphertext()
    blocks = [encrypted_flag[i:i + 32] for i in range(0, len(encrypted_flag), 32)]
    initialization_vectors = blocks[:-1]
    ciphertext_blocks = blocks[1:]

    decrypted_blocks = [decrypt_and_xor(ciphertext_block, iv) for ciphertext_block, iv in zip(ciphertext_blocks, initialization_vectors)]

    decrypted_flag = "".join(decrypted_blocks)
    print(decrypted_flag)

if __name__ == "__main__":
    main()