from github import Github
from github import GithubException


class GitHubApiService:

    def __init__(self, api_token, api_user):
        self.__api_user = api_user
        self.__github_conn = Github(api_token)

    def delete_all_account_repos(self) -> bool:
        try:
            user = self.__github_conn.get_user(self.__api_user)
            for repo in user.get_repos():
                repo.delete()
            return True
        except GithubException:
            return False
