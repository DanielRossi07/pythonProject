import datetime
import sqlite3
from cryptography.fernet import Fernet

KEY = b'oVLz9iF1e31dz2uwhZ1F6Nhh84avpebhP-yhcetOn1U='


class DataBase:
    def __init__(self):
        self.filename = "cryptoconverter.db"
        self.connection = sqlite3.connect(self.filename)
        self.cursor = self.connection.cursor()

    def verify_if_exists(self, username):
        user = self.cursor.execute(f"SELECT * FROM users WHERE username='{username}'").fetchone()

        if user is None:
            return False

        return True

    def validate_user(self, username, password):
        user = self.cursor.execute(f"SELECT * FROM users WHERE username='{username}'").fetchone()
        if not user:
            return False

        hash_password = user[1]
        _password = self.decrypt(hash_password)

        if _password != password:
            return False

        return True

    def add_user(self, username, password):
        if self.verify_if_exists(username):
            return False

        hash_password = self.encrypt(password)

        self.cursor.execute(f"insert into users (username, password) values ('{username}', '{hash_password}')")
        self.connection.commit()

        return True

    def encrypt(self, password):
        encrypter = Fernet(KEY)
        hash_password = encrypter.encrypt(password.encode())
        return hash_password.decode()

    def decrypt(self, hash_password):
        decrypter = Fernet(KEY)
        password = decrypter.decrypt(hash_password.encode())
        return password.decode()

