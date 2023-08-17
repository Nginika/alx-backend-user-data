#!/usr/bin/env python3
"""authorization module"""
import bcrypt


def _hash_password(password: str) -> str:
    """hashes password to bytes"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
