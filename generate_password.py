import random
import string

def generate_password():
    seed = "FLAG{Peek_into_the_past}"
    random.seed(seed)
    
    length = 12

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password