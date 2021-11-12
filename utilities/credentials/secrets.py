import os


class Secrets:
    EMAIL = os.environ.get("EMAIL_GIT_TEST")
    USERNAME = os.environ.get("USER_GIT_TEST")
    PASSWORD = os.environ.get("PASSWORD_GIT_TEST")
    TOKEN = os.environ.get("TOKEN_GIT_TEST")
