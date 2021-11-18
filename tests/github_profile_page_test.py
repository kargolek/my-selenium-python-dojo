import pytest
import pytest_check as check

from utilities.credentials.secrets import Secrets


@pytest.mark.usefixtures("login_to_github_account", "set_cookies", "add_cookies")
class TestGitHubProfilePage:
    name = "Joe Doe"
    bio = "I like fish and chips.\nBTC is a king"
    company = "Sweet Dreams IT Solution"
    location = "Piaseciuset"
    website = "http://google.com"
    twitter_id = "kargolek"

    def test_edit_profile_should_save_all_details(self, github_profile_land_page):
        profile_component_page = github_profile_land_page.open_url(Secrets.USERNAME) \
            .profile_component_page.click_edit_button() \
            .input_name(self.name) \
            .input_bio(self.bio) \
            .input_company(self.company) \
            .input_location(self.location) \
            .input_website_blog(self.website) \
            .input_twitter_id(self.twitter_id) \
            .click_save_edit_info()

        check.equal(profile_component_page.get_name_user_detail_text(), self.name)
        check.equal(profile_component_page.get_account_name_detail_text(), Secrets.USERNAME)
        check.equal(profile_component_page.get_bio_detail_text(), self.bio.replace("\n", " "))
        check.equal(profile_component_page.get_company_detail_text(), self.company)
        check.equal(profile_component_page.get_location_detail_text(), self.location)
        check.equal(profile_component_page.get_website_blog_detail_text(), self.website)
        check.equal(profile_component_page.get_twitter_detail_text(), f"@{self.twitter_id}")
