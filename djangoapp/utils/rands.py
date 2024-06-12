#GERAR NUMEROS ALEATORIOS!!
from random import SystemRandom
import string
from django.utils.text import slugify

def random_letter(k=5):
    return ''.join(SystemRandom().choices(
        string.ascii_lowercase + string.digits,
        k=k
    ))

def slugify_new(text):
    return slugify(text) + '-' + random_letter(2)

print(slugify_new('bla bla bla atencao'))