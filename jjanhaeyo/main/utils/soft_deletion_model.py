import random
import string


def random_string(length=16, punctutaions=False):
    letters = string.ascii_letters + string.digits
    if punctutaions:
        letters += '!@#$^&'
    return ''.join(random.SystemRandom().choice(letters) for _ in range(length))


def random_image(filename='test.png'):
    from PIL import Image
    size = (200,200)
    color = (255,0,0,0)
    img = Image.new("RGBA",size,color)
    from io import BytesIO
    f = BytesIO()
    img.save(f, 'png')
    f.name = 'test.png'
    f.seek(0)
    return f
