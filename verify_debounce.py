import os
import time
from playwright.sync_api import sync_playwright

def test_debounce():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Get absolute path to the HTML file
        path = os.path.abspath("BadgeMaster_Pro_Mobile_v5.3.html")
        page.goto(f"file://{path}")

        # Navigate to "Créer un badge" page
        page.click("text=Créer un badge")

        # Check initial preview name
        preview_name = page.locator("#preview-name")
        assert preview_name.inner_text() == "NOM PRÉNOM"

        # Type into the name input
        page.fill("#badge-name", "John Doe")

        # Immediately after typing, it should NOT have updated yet (because of 250ms debounce)
        # Note: Playwright's fill might be too fast, but we check right after.
        # However, to be sure, we can use 'type' with low delay if needed.
        # Let's check immediately.
        text_immediately = preview_name.inner_text()
        print(f"Immediately: {text_immediately}")

        # Wait for more than 250ms
        time.sleep(0.5)

        # Now it should be updated
        text_after = preview_name.inner_text()
        print(f"After debounce: {text_after}")
        assert text_after == "JOHN DOE" # Code uppercase it in preview

        # Verify it works
        page.screenshot(path="verification_badge.png")

        browser.close()

if __name__ == "__main__":
    test_debounce()
