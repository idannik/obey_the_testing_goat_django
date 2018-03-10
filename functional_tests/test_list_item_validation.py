from selenium.webdriver.common.keys import Keys
from unittest import skip
from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):
    @skip
    def test_cannot_add_empyty_list_items(self):
        # Edith goes to the home page and accidentally tries to submit
        # an empty list item. she  hits enter on the empty input box
        # the home page refreshes, and there is an error message sying
        # that list items cannot be blank
        # She tries again with some text for the item
        # which now works
        # She receives a similar warning on the list page
        # And she can correct it by filling some text in
        self.fail("write me")
