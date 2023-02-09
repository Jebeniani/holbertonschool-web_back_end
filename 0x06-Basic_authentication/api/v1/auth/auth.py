#!/usr/bin/env python3
"""Module of Auth"""
from flask import request
from typing import List, TypeVar


class Auth():
    """api authentication manager"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Return False - path and excluded_paths will be used later"""
        return False

    def authorization_header(self, request=None) -> str:
        """Return None - request will be the Flask request object"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Return None - request will be the Flask request object"""
        return None
