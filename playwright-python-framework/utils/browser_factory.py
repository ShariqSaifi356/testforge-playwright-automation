from playwright.sync_api import sync_playwright


class BrowserFactory:

    def __init__(self):
        self.playwright = sync_playwright().start()

    def create_browser(self):
        return self.playwright.chromium.launch(
            headless=False
        )

    def create_context(self, browser):
        context = browser.new_context()
        context.route("**/*", self.block_ads)
        return context

    def block_ads(self, route):

        url = route.request.url.lower()

        ad_keywords = [
            "doubleclick",
            "googlesyndication",
            "googleadservices",
            "adservice",
            "adsystem",
            "adnxs",
            "taboola",
            "outbrain"
        ]

        if any(keyword in url for keyword in ad_keywords):
            route.abort()
        else:
            route.continue_()

    def close(self, browser, context):
        context.close()
        browser.close()
        self.playwright.stop()