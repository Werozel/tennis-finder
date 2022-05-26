"""This module contains hash functions used for crypto purposes."""
import binascii
import hashlib

from tennis_finder.config import salt


def hash_password(s: str, user_login: str):
    """
    Get a password hash.

    :param s: User password
    :param user_login: User login
    :return: hash password string
    """
    tmp: str = binascii.hexlify(hashlib.pbkdf2_hmac('md5', str.encode(s), str.encode(salt), 2**16)).decode()
    return binascii.hexlify(hashlib.pbkdf2_hmac('sha256', str.encode(tmp), str.encode(user_login), 2**16)).decode()
