from base64 import b64decode


class Decrypter:
    def __init__(self, private_key: int, product: int):
        self._private_key = private_key
        self.product = product

    def __str__(self):
        return f'Decrypter{{ {self._private_key},{self.product} }}'

    def decrypt(self, encrypted_message: int) -> int:
        return pow(encrypted_message, self._private_key, self.product)

    def decrypt_string(self, encrypted_message: str) -> str:
        message_b64 = b64decode(encrypted_message.encode('utf-8'))
        message = []
        for i in range(0, len(message_b64), 8):
            message.append(self.decrypt(int.from_bytes(message_b64[i:i+8], 'big')))

        return bytes(message).decode('utf-8')
