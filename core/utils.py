import base64
import os
import pprint
import time
from functools import wraps
from typing import List

from cryptography.fernet import Fernet
from django.conf import settings
from django.http import Http404


def which_settings() -> str:
    """
    returns 'local' or 'production', etc.
    """
    s = os.environ.get("DJANGO_SETTINGS_MODULE")
    return s.rsplit(".")[-1]


def timeit(func):
    @wraps(func)
    def closure(*args, **kwargs):
        ts = time.time()
        result = func(*args, **kwargs)
        te = time.time()
        print("<%s> took %0.3fs." % (func.__name__, te - ts))
        return result

    return closure


def encrypt(password: str) -> str:
    # https://github.com/pyca/cryptography
    secret_key = settings.SECRET_KEY
    key = base64.urlsafe_b64encode(secret_key.encode()[:32])

    f = Fernet(key)
    token = f.encrypt(password.encode())
    password = token.decode()
    # return password, key.decode()
    return password


def decrypt(password: str) -> str:
    # https://github.com/pyca/cryptography
    secret_key = settings.SECRET_KEY
    key = base64.urlsafe_b64encode(secret_key.encode()[:32])

    f = Fernet(key)
    byte_decrypted = f.decrypt(password.encode())
    return byte_decrypted.decode()


def get_all_fields(model) -> List[str]:
    # print('---------------------------')
    # pprint.pprint(model._meta.__dict__)
    # print('---------------------------')

    r = []
    try:
        # r = [f.name for f in model._meta.__dict__["local_fields"]]
        r = [f.name for f in model._meta.local_fields]
    except KeyError:
        pass
    else:
        pass
    return r


def get_all_fields_excluding(model, exclude_list: List[str]) -> List[str]:
    if type(exclude_list) is not list:
        raise TypeError("exclude_list must be list")

    include_list = get_all_fields(model)

    for i in include_list:
        for e in exclude_list:
            e = e.strip()
            if e in include_list:
                include_list.remove(e)

    return include_list


def superuser_check(user):
    """To be used as parameter for @user_passes_test
    View is only available for superuser otherwise raise 404"""
    if user.is_superuser:
        return True
    raise Http404()


def staff_check(user):
    """To be used as parameter for @user_passes_test
    View is only available for staff otherwise raise 404"""
    if user.is_staff:
        return True
    raise Http404()
