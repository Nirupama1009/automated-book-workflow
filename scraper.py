from playwright.sync_api import sync_playwright

def scrape_and_screenshot(
    url="https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1",
    screenshot_file="screenshot.png",
    html_file="chapter.html"
):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)

        # Wait until the content loads
        page.wait_for_selector("div#mw-content-text")

        # Take full-page screenshot
        page.screenshot(path=screenshot_file, full_page=True)

        # Get the HTML of the main content
        content = page.inner_html("div#mw-content-text")
        with open(html_file, "w", encoding="utf-8") as f:
            f.write(content)

        browser.close()
        print("[✓] Screenshot and chapter content saved.")

if __name__ == "__main__":
    scrape_and_screenshot()
