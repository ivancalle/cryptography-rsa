from base64 import b64encode


class Encrypter:
    def __init__(self, public_key: int, product: int):
        self.public_key = public_key
        self.product = product

    def __str__(self):
        return f'Encrypter{{ {self.public_key},{self.product} }}'

    def encrypt(self, message: int) -> int:
        if message < self.product:
            return pow(message, self.public_key, self.product)

        raise Exception('Message is congruent with another number')

    def encrypt_string(self, message: str) -> str:
        encrypted_message: list = []
        for byte in message.encode('utf-8'):
            encrypted_message += self.encrypt(byte).to_bytes(8, 'big')

        return b64encode(bytes(encrypted_message)).decode('utf-8')
