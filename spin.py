import random
import string
def spin(len: int):
    n=string.ascii_letters+string.digits
    return''.join(random.choices(n, k=len))  
print(spin(1))