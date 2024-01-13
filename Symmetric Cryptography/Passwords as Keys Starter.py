from Crypto.Cipher import AES
import hashlib
import codecs

def read_wordlist(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        return [w.strip() for w in f.readlines()]

def decrypt(ciphertext, password_hash):
    try:
        ciphertext = bytes.fromhex(ciphertext)
        key = bytes.fromhex(password_hash)

        cipher = AES.new(key, AES.MODE_ECB)
        decrypted = cipher.decrypt(ciphertext)

        return {"plaintext": decrypted.hex()}
    except ValueError as e:
        return {"error": str(e)}

def main():
    file_path = "/usr/share/wordlists/rockyou.txt"
    wordlist = read_wordlist(file_path)

    FLAG = "c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66"

    for word in wordlist:
        pass_hash = hashlib.md5(word.encode()).hexdigest()
        dec = decrypt(FLAG, pass_hash)
        
        try:
            decrypted_text = codecs.decode(dec['plaintext'], 'hex').decode('ascii')
            print(decrypted_text)
            break
        except UnicodeDecodeError:
            continue

if __name__ == "__main__":
    main()