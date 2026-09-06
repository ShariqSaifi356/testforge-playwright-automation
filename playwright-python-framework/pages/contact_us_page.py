from pages.base_page import BasePage


class ContactUsPage(BasePage):

    def __init__(self, page, logger):
        super().__init__(page, logger)

        self.contact_heading = page.get_by_role("heading", name="Get In Touch", exact=True)
        self.name = page.get_by_placeholder("Name", exact=True)
        self.email = page.get_by_placeholder("Email", exact=True)
        self.subject = page.get_by_placeholder("Subject", exact=True)
        self.message = page.get_by_placeholder("Your Message Here", exact=True)
        self.file_input = page.locator("input[type='file'][name='upload_file']")
        self.submit_button = page.get_by_role("button", name="Submit", exact=True)
        self.success_message = page.locator("div.status").filter(has_text="Success! Your details have been submitted successfully.")
        self.home_button = page.locator("#form-section").get_by_role("link", name="Home")

    def enter_name(self, name:str):
        self.fill(self.name, name)

    def enter_email(self, email:str):
        self.fill(self.email, email)

    def enter_subject(self, subject:str):
        self.fill(self.subject, subject)

    def enter_message(self, message:str):
        self.fill(self.message, message)

    def upload_attachment(self, file_path):
        self.upload_file(self.file_input, file_path)

    def click_submit_button(self):
        self.wait_for_page_load()
        self.click(self.submit_button)

    def click_home_button(self):
        self.click(self.home_button)
