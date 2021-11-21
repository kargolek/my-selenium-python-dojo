from hamcrest import assert_that, is_

from tests.conftest import on_firefox_skip


class TestHerokuAppJavascriptError:

    # check it if js error occurred, skipped for firefox.
    @on_firefox_skip
    def test_handle_assertion_for_javascript_errors_example(self, heroku_app_javascript_error_page, driver_utils):
        heroku_app_javascript_error_page.open_url().is_url_is_set()
        assert_that(driver_utils.is_severe_console_log_occurred("javascript"), is_(True))
