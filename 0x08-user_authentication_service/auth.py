#!/usr/bin/env python3
"""Hash password"""
from db import DB
import bcrypt
from sqlalchemy.orm.exc import NoResultFound
from user import User
from uuid import uuid4


def _hash_password(password: str) -> str:
    """returning a salted hash of the password"""
    salt = bcrypt.gensalt()

    return bcrypt.hashpw(password.encode('utf-8'), salt)


def _generate_uuid() -> str:
    """generating UUIDss"""
    return str(uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a new user with the provided email and password"""
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            hash = _hash_password(password)
            user = self._db.add_user(email, hash)
            return user
        else:
            raise ValueError(f"User {email} already exists.")

    def valid_login(self, email: str, password: str) -> bool:
        """locating the user by email"""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        return bcrypt.checkpw(password.encode('utf-8'), user.hashed_password)

    def create_session(self, email: str) -> str:
        """find the user that corresponds to the given email"""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None
        session_id = _generate_uuid()
        self._db.update_user(user.id, session_id=session_id)
        return session_id
