"""This module contains functions that process incoming args."""
from flask import request, abort
import logging


def get_cookie(key: str, default):
    """Get cookie from a request."""
    res = request.cookies.get(key)
    return res if res is not None else default


def get_arg_or_400(arg: str, to_int: bool = False):
    """Get arg from request or throw code 400."""
    try:
        res = request.args.get(arg)
        if res is None:
            raise ValueError(f"No such argument: '{arg}'")
        return int(res) if to_int else res
    except ValueError as e:
        logging.error(e)
        abort(400)


def get_arg_or_none(arg: str, to_int: bool = False):
    """Get arg from request or None."""
    try:
        res = request.args.get(arg)
        return int(res) if res and to_int else res
    except ValueError:
        return None
