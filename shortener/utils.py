import random
import string

def code_generator(size=6, char=string.ascii_lowercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))