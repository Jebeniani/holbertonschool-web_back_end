#!/usr/bin/env python3
"""filtered_logger"""
import re
import os
from typing import List
import logging
import mysql.connector


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


def get_logger() -> logging.Logger:
    """the get_logger function uses the logging.getLogger method
    to get a logger object with the name "user_data"""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    formatter = RedactingFormatter(PII_FIELDS)
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """function that returns a connector to the database"""
    host = os.environ.get("PERSONAL_DATA_DB_HOST", "localhost")
    username = os.environ.get("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.environ.get("PERSONAL_DATA_DB_PASSWORD", "")
    db_name = os.environ.get("PERSONAL_DATA_DB_NAME")

    if not db_name:
        raise ValueError("PERSONAL_DATA_DB_NAME environment variable not set")

    return mysql.connector.connect(
        host=host,
        user=username,
        password=password,
        database=db_name
    )


def main():
    """function will obtain a database connection using get_db and retrieve
    all rows in the users table and display each row under a filtered format"""
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    for row in rows:
        name = row[0]
        email = row[1]
        phone = row[2]
        ssn = row[3]
        password = row[4]
        ip = row[5]
        last_login = row[6]
        user_agent = row[7]
        print("[HOLBERTON] user_data INFO 2019-11-19 18:37:59,596: name={};" +
              "email={}; phone={}; ssn={}; password={}; ip={};" +
              "last_login={}; user_agent={};"
              .format(name, email, phone, ssn,
                      password, ip, last_login, user_agent))


if __name__ == '__main__':
    main()
