#!/usr/bin/env python3
"""returns a log message obfuscated"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str):
    """function that filters data and hides some"""
    for field in fields:
        message = re.sub(rf"{field}=(.*?)\{separator}",
                         f'{field}={redaction}{separator}', message)
    return message
