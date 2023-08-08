#!/usr/bin/env python3
"""API authentication class"""
import flask
from flask import request
from typing import List, TypeVar


class Auth():
    """Authentication class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """checks if authorization is required"""
        check = path
        if path is None:
            return True
        if excluded_paths is None or []:
            return True
        if path[-1] != "/":
            check += "/"
        if check in excluded_paths or path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """create header with authorization details"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """get the current user """
        return None
