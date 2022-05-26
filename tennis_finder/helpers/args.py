"""This module contains functions that process incoming args."""
from flask import request, abort
import logging


def get_cookie(key: str, default):
    """
    Get cookie from a request.

    :param key: string with key of a cookie
    :param default: any fallback value
    :return: value of a cookie or a fallback
    """
    res = request.cookies.get(key)
    return res if res is not None else default


def get_arg_or_400(arg: str):
    """
    Get arg from request or throw code 400.

    :param arg: str with a key of an argument to get
    :return: value of an argument with given key
    """
    try:
        res = request.args.get(arg)
        if res is None:
            raise ValueError(f"No such argument: '{arg}'")
        return res
    except ValueError as e:
        logging.error(e)
        abort(400)


def get_arg_or_none(arg: str):
    """
    Get arg from request or None.

    :param arg: str with a key of an argument to get
    :return: value of an argument with given key or None
    """
    try:
        return request.args.get(arg)
    except ValueError:
        return None
