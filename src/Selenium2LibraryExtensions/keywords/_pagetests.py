#from selenium.webdriver.common.keys import Keys
#from Selenium2Library import utils
#from Selenium2Library.locators import ElementFinder
#from Selenium2Library.keywords.keywordgroup import KeywordGroup
#from Selenium2Library.keywords import _ElementKeywords

from robot.libraries.BuiltIn import BuiltIn

class _PageTestsKeywords():
    """ Runs assertions against the content of the page.
    Returns booleans instead of throwing errors
    """

    def is_visible(self, locator):
        """Same than Element Should Be Visible but returns a boolean """
        selenium2lib = BuiltIn().get_library_instance('Selenium2Library')
        try:
          return selenium2lib.element_should_be_visible(locator)
        except AssertionError:
          return False

    def is_element_present(self, locator):
        """Same than Page Should Contain Element but returns a boolean """
        selenium2lib = BuiltIn().get_library_instance('Selenium2Library')
        try:
          return selenium2lib.page_should_contain_element(locator)
        except AssertionError:
          return False

    def select_iframe(self, locator):
        """Sets iframe identified by `locator` as current frame.

        Key attributes for frames are `id` and `name.` See `introduction` for
        details about locating elements.
        """
        selenium2lib = BuiltIn().get_library_instance('Selenium2Library')
        selenium2lib._info("Selecting iframe '%s'." % locator)
        element = selenium2lib._element_find(locator, True, True, tag='iframe')
        selenium2lib._current_browser().switch_to_frame(element)



