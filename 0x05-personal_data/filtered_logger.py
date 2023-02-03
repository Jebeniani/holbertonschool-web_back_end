#!/usr/bin/env python3
"""filtered_logger"""
import re
from typing import List
import logging


PII_FIELDS = ("name", "email", "phone", "ssn", "password",)


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """ function that returns the log message obfuscated """
    for i in fields:
        message = re.sub(rf'{i}=(.*?)\{separator}',
                         f'{i}={redaction}{separator}', message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Initializer"""
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """an updated method to filter values in the incoming log records"""
        return filter_datum(
            self.fields, self.REDACTION,
            super().format(record), self.SEPARATOR)
