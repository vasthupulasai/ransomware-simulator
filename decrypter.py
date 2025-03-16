from cryptography.fernet import Fernet
import os

def load_key():
    return open("encryption.key", "rb").read()

def decrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(file_path, "wb") as file:
        file.write(decrypted_data)

def decrypt_files_in_directory(directory, key):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            decrypt_file(file_path, key)
            print(f"Decrypted: {file_path}")

if __name__ == "__main__":
    key = load_key()
    decrypt_files_in_directory("test_files", key)
    print("Decryption complete!")
