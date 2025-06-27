from cryptography.fernet import Fernet

def encrypt_message(message_decrypter_version, key):
    fernet = Fernet(key)
    return fernet.encrypt(message_decrypter_version.encode())

def decrypt_message(message_encrypted_version, key):
    fernet = Fernet(key)
    return fernet.decrypt(message_encrypted_version).decode()
