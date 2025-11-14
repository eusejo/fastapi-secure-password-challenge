import string
from random import choice

def gerador(senha: str = '') -> str:
    chars = string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation

    for _ in range(12):
        senha += choice(chars[:])
    return senha