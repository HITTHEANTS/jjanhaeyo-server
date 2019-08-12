from io import BytesIO
from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile


def image_thumbnail(fp, size=(100,100)):
    if fp.content_type == 'image/jpeg':
        filename = 'thumbnail.jpg'
        fileformat = 'JPEG'
    elif fp.content_type == 'image/png':
        filename = 'thumbnail.png'
        fileformat = 'PNG'
    else:
        raise Exception('Unsupported file type: {}'.format(fp.content_type))

    image = Image.open(fp)
    fp.seek(0)

    image.thumbnail(size, Image.ANTIALIAS)

    thumb_io = BytesIO()
    image.save(thumb_io, format=fileformat)
    thumb_io.seek(0)

    return SimpleUploadedFile(filename, thumb_io.read(), content_type=fp.content_type)
