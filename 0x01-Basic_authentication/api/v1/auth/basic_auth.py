#!/usr/bin/env python3
"""the basic auth class"""
from api.v1.auth.auth import Auth
import base64


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
