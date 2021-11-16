import time
import traceback

from github import Github
from github import GithubException

from utilities.logger.test_logger.test_step import step


class GitHubApiService:

    def __init__(self, api_token, api_user):
        self.__api_user = api_user
        self.__github_conn = Github(login_or_token=api_token)

    @step
    def api_call_delete_all_account_repos(self) -> bool:
        try:
            repos = self.__github_conn.get_user().get_repos()
            for repo in repos:
                time.sleep(0.2)
                repo.delete()
            return True
        except GithubException:
            print(traceback.format_exc())
            return False

    @step
    def api_call_create_repo(self, repo_name: str, private=False) -> bool:
        try:
            self.__github_conn.get_user().create_repo(name=repo_name, private=private)
            return True
        except GithubException:
            print(traceback.format_exc())
            return False

    @step
    def get_repos(self):
        return self.__github_conn.get_user().get_repos()
