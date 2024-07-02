import random
import string

def generate_password(length):
    """
    Generate a password of the specified length using a combination of random characters.
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
