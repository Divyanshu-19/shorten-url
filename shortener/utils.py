import random
import string

# from shortener.models import shortURL

def code_generator(size=6, chars=string.ascii_lowercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))


def create_shortcode(instance, size=6):
	new_code = code_generator(size=size)
	klass = instance.__class__
	qs = klass.objects.filter(shortcode=new_code).exists()
	if qs:
		return create_shortcode(instance, size=size)
	return new_code