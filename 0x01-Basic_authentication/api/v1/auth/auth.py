#!/usr/bin/env python3
"""API authentication class"""
import flask
from flask import request
from typing import List, TypeVar


class Auth():
    """Authentication class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """checks if authorization is required"""
        return False

    def authorization_header(self, request=None) -> str:
        """create header with authorization details"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """get the current user """
        return None
