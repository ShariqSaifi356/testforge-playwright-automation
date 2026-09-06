from pages.base_page import BasePage


class TestCasesPage(BasePage):
    __test__ = False

    def __init__(self, page, logger):
        super().__init__(page, logger)

        self.test_cases_heading = page.get_by_role("heading", name="Test Cases", exact=True)
