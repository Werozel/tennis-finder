from flask import request


def get_cookie(key: str, default):
    res = request.cookies.get(key)
    return res if res is not None else default
