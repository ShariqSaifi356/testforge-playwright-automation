from pathlib import Path

from playwright.sync_api import sync_playwright


FRAMEWORK_DIR = Path(__file__).resolve().parent.parent
VIDEO_DIR = FRAMEWORK_DIR / "screenshots" / "videos"


class BrowserFactory:

    def __init__(self):
        self.playwright = sync_playwright().start()

    def create_browser(self, browser_name):
        if browser_name == "chromium":
            return self.playwright.chromium.launch(headless=False)

        elif browser_name == "firefox":
            return self.playwright.firefox.launch(headless=False)

        elif browser_name == "webkit":
            return self.playwright.webkit.launch(headless=False)

    def create_context(self, browser):
        VIDEO_DIR.mkdir(parents=True, exist_ok=True)
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            record_video_dir=str(VIDEO_DIR),
            record_video_size={"width": 1920, "height": 1080}
        )
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