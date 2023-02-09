#!/usr/bin/env python3
"""creating a session"""
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """updating sessionauth class"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """method that creates a session idfor a user_id"""
        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """method that returns a User id based on a session ID"""
        if session_id is None or not isinstance(session_id, str):
            return None

        return self.user_id_by_session_id.get(session_id)
