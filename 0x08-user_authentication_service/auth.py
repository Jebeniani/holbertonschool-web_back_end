#!/usr/bin/env python3
"""Hash password"""
import bcrypt


def _hash_password(password: str) -> str:
    """returning a salted hash of the password"""
    salt = bcrypt.gensalt()

    return bcrypt.hashpw(password.encode('utf-8'), salt)
