#!/usr/bin/env python3
"""Basic Auth"""
from api.v1.auth.auth import Auth
from base64 import b64decode


class BasicAuth(Auth):
    """BasciAuth class"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """a method that returns the Base64 part of the Authorization"""
        if authorization_header is None or not isinstance(authorization_header,
                                                          str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header.split("Basic ")[1]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """ a method returns the decoded value of a Base64 string """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            baseEncode = base64_authorization_header.encode('utf-8')
            baseDecode = b64decode(baseEncode)
            decodedValue = baseDecode.decode('utf-8')
            return decodedValue
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """ returns the user email and
        password from the Base64 decoded value"""
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ":" not in decoded_base64_authorization_header:
            return None, None
        credentials = decoded_base64_authorization_header.split(":", 1)
        return credentials[0], credentials[1]
