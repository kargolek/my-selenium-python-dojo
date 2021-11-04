import os


class Environment:
    IS_CI_CD_ENV = os.environ.get("GITHUB_ACTIONS")
