from github import Github

from utilities.credentials.secrets import Secrets


class GitHubApiService:

    def __init__(self, api_token, api_user):
        self.api_token = api_token
        self.api_user = api_user
        self.__github_conn = Github(api_token)

    def delete_all_account_repos(self):
        self.__github_conn.rate_limiting_resettime
        user = self.__github_conn.get_user(Secrets.USERNAME)
        for repo in user.get_repos():
            print(repo)