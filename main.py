import random
import string

def pass_gen(length):
    """
    Generates a secure password of the specified length.
    
    Args:
        length (int): The desired length of the password.

    Returns:
        str: Generated password.
    """
    allowed_char = string.ascii_letters + string.digits + string.punctuation

    if length <=0:
        raise ValueError('The length of the password must be greater than 0.')
    else:
        return ''.join(random.choice(allowed_char) for i in range(length))

try:
    len = int(input('Introduce the desired length to generate a secure password: '))
    passwd = pass_gen(len)
    print(passwd)
except ValueError as e:
    print('Error:', e)