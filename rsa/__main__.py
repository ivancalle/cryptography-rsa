import argparse

from .key_generator import KeyGenerator
from .encrypter import Encrypter
from .decrypter import Decrypter
from .utils import break_key

parser = argparse.ArgumentParser(prog='rsa')
group = parser.add_mutually_exclusive_group()
group.add_argument('--generate-key', '-g', action='store_true', help='Generate key')
group.add_argument('--decrypt', '-d', help='Decrypt key,product')
group.add_argument('--encrypt', '-e', help='Encrypt key,product')
parser.add_argument('--message', '-m', help='Message')
parser.add_argument('--is-int', '-i', action='store_true', help='message is integer')
group.add_argument('--break-key', '-b', help='Decrypt key,product')


args = parser.parse_args()

if args.generate_key:
    encrypter, decrypter = KeyGenerator().get_encrypters()
    print(encrypter)
    print(decrypter)
elif args.decrypt and args.message:
    decripter = Decrypter(*(int(x) for x in args.decrypt.split(',')))
    if args.is_int:
        print(decripter.decrypt(int(args.message)))
    else:
        print(decripter.decrypt_string(args.message))

elif args.encrypt and args.message:
    # due to the prime numbers are low, this are wrong if message is not coprime with prime numbers
    encrypter = Encrypter(*(int(x) for x in args.encrypt.split(',')))
    if args.is_int:
        print(encrypter.encrypt(int(args.message)))
    else:
        print(encrypter.encrypt_string(args.message))
elif args.break_key:
    private_key, product = break_key(*(int(x) for x in args.break_key.split(',')))
    print(Decrypter(private_key, product))
