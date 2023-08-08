#!/usr/bin/env python3
"""the basic auth class"""
from api.v1.auth.auth import Auth
import base64
import binascii


class BasicAuth(Auth):
    """basic authorization methods"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """extracts the authorization code"""
        if (authorization_header is None or not
                isinstance(authorization_header, str)):
            return None
        if authorization_header[0:6] != 'Basic ':
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """decodes base 64 string"""
        if (base64_authorization_header and
                isinstance(base64_authorization_header, str)):
            try:
                encode = base64_authorization_header.encode('utf-8')
                base = base64.b64decode(encode)
                return base.decode('utf-8')
            except binascii.Error:
                return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """get user details from base64 decoded valuee"""
        decode_64 = decoded_base64_authorization_header
        if (decode_64 and isinstance(decode_64, str) and ":" in decode_64):
            result = decode_64.split(":", 1)
            return (result[0], result[1])
        return (None, None)
