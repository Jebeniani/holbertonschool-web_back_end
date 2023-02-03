#!/usr/bin/env python3
"""Regex-ing"""
import re
from typing import List

PII_FIELDS = ("name", "email", "phone", "ssn", "password",)


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """ function that returns the log message obfuscated """
    for i in fields:
        message = re.sub(f'{i}=.*?{separator}',
                         f'{i}={redaction}{separator}', message)
    return message
