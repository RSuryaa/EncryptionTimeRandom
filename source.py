from cryptography.fernet import Fernet

def encrypt_message(string_message, key):
    fernet = Fernet(key)
    return fernet.encrypt(string_message.encode())

def decrypt_message(message_encrypted_version, key):
    fernet = Fernet(key)
    return fernet.decrypt(message_encrypted_version).decode()
