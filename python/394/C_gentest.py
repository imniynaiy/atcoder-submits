import random

def generate_random_string():
    length = random.randint(1, 100)
    characters = 'AWC'
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

# Example usage
print(generate_random_string())