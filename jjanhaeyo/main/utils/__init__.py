from .random import *
from .image import *
from .soft_deletion_model import *

from django.conf import settings


def deepEqual(a, b):
    if a == b:
        return True

    elif isinstance(a, dict) and isinstance(b, dict):
        if len(a) != len(b): return False
        for k, v in a.items():
            if k not in b: return False
            if b[k] != v:
                if type(b[k]) != type(v): return False
                elif isinstance(v, list) or isinstance(v, dict):
                    return deepEqual(b[k], v)
                else: return False
        return True

    elif isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b): return False
        for i, v in enumerate(a):
            if b[i] != v: return False
        return True

    return False


def make_absolute_uri(url):
    if url.startswith('http://') or url.startswith('https://'):
        return url.split('?')[0]
    return settings.CDN_URL + url


def make_null(instance, fields=[]):
    for field in fields:
        v = getattr(instance, field)
        if v == '' or v == {}:
            setattr(instance, field, None)
