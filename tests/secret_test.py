import os

from hamcrest import assert_that, equal_to


class TestSecret:

    def test_secret(self, web_driver_each, web_driver_each_quit):
        print(os.environ)
        assert_that(os.environ.get("EMAIL_GIT_TEST"), equal_to("example"))
