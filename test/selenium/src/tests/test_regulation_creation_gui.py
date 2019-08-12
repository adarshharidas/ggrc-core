# Copyright (C) 2019 Google Inc.
# Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>
"""Login page smoke tests."""
# pylint: disable=no-self-use
import pytest
from lib import base, url
from lib.constants import locator
from lib.utils import selenium_utils
class TestLoginPage(base.Test):
    """Tests for login page."""
    @pytest.mark.smoke_tests
    def test_login_as_admin(self, selenium):
        """Logs in and verifies that we're logged in as admin."""
        # Login to the GGRC.
        selenium_utils.open_url(url.Urls().login)
        selenium.find_element(*locator.PageHeader.BUTTON_ADMIN_DASHBOARD)
        # Click the create object button.
        selenium.find_element(*locator.Dashboard.CREATE_OBJECT_BTN_CSS).click()
        # TODO Find regulations button and click
        selenium.find_element(
            *locator.CreateObjectDropdown.CREATE_REGULATION_BTN_CSS).click()
        # TODO Fill title
        selenium.find_element(
            *locator.CreateObjectDropdown.TITLE_TEXTBOX_CSS).\
            send_keys("provide your title")
        # TODO Fill description
        selenium.find_element(
            *locator.CreateObjectDropdown.DESCRIPTION_TEXTBOX_CSS).\
            send_keys("provide your description")
        # Click save and close button.
        selenium.find_element(
            *locator.ModalCreateNewObject.BUTTON_SAVE_AND_CLOSE).click()
        # find current url
        after_regulation_creation = selenium.getCurrentUrl()
        # Click add tab button.
        selenium.find_element(
            *locator.Regulation.REGULATION_ADD_TAB_BTN_CSS).click()
        # Click products button.
        selenium.find_element(
            *locator.AddTabDropdown.ADD_TAB_PRODUCTS_BTN_CSS).click()
        # find current url
        after_add_tab = selenium.getCurrentUrl()
        # Compare the url's
        assert after_regulation_creation == after_add_tab, \
            "The url after creating object and after adding tab are different."
