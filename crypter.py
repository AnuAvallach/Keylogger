from cryptography.fernet import Fernet


class Crypter:

    def __init__(self):
        self.__key = Fernet.generate_key()

    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, value):
        self.__key = value

    def generate_new_key(self):
        """
        This function will generate a new key for Fernet.

        """

        self.__key = Fernet.generate_key()

    def encrypt(self, message):
        """
        This function encrypts the given message using Fernet.

        :param message: Message to encrypt
        :return: Encrypted message
        """

        encoded_message = message.encode()
        fernet = Fernet(self.key)
        encrypted_message = fernet.encrypt(encoded_message)
        return encrypted_message

    def decrypt(self, message):
        """
        This function decrypts the given message using Fernet.

        :param message: Message to decrypt
        :return: Decrypted message
        """

        fernet = Fernet(self.key)
        decrypted_message = fernet.decrypt(message)
        decoded_message = decrypted_message.decode()
        return decoded_message
