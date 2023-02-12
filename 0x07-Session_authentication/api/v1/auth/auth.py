#!/usr/bin/env python3
"""Module of Auth"""
from flask import request
from typing import List, TypeVar
import os


class Auth():
    """api authentication manager"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Return False - path and excluded_paths will be used later"""
        class Auth:
            def require_auth(self, path: str, excluded_paths:
                             List[str]) -> bool:
                if not path:
                    return True
        if not excluded_paths or len(excluded_paths) == 0:
            return True
        for excluded_path in excluded_paths:
            if path == excluded_path or path.startswith(excluded_path[:-1]):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """Return None - request will be the Flask request object"""
        if request is None:
            return None
        if "Authorization" not in request.headers:
            return None
        return request.headers["Authorization"]

    def current_user(self, request=None) -> TypeVar('User'):
        """Return None - request will be the Flask request object"""
        return None

    def session_cookie(self, request=None):
        """a method that returns a cookie value from a request"""
        if request is None:
            return None

        session_name = os.environ.get('SESSION_NAME', '_my_session_id')
        return request.cookies.get(session_name)
